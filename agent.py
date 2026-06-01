"""
Stock analysis agent using IBM watsonx.ai (LLM) + Tavily (web search).
Produces a structured report with BUY / HOLD / SELL recommendation.
"""

import os
from ibm_watsonx_ai import APIClient, Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.foundation_models.schema import TextChatParameters
from tavily import TavilyClient

# ---------------------------------------------------------------------------
# Clients
# ---------------------------------------------------------------------------

def _wx_client() -> ModelInference:
    creds = Credentials(
        url=os.environ["WATSONX_URL"],
        api_key=os.environ["WATSONX_APIKEY"],
    )
    client = APIClient(creds)
    params = TextChatParameters(
        temperature=0.2,
        max_tokens=2048,
    )
    return ModelInference(
        model_id=os.environ.get("WATSONX_MODEL", "meta-llama/llama-3-3-70b-instruct"),
        api_client=client,
        project_id=os.environ["WATSONX_PROJECT_ID"],
        params=params,
    )


def _tavily_client() -> TavilyClient:
    return TavilyClient(api_key=os.environ["TAVILY_API_KEY"])


# ---------------------------------------------------------------------------
# Search helpers
# ---------------------------------------------------------------------------

def search_company(tavily: TavilyClient, ticker: str, company_name: str) -> str:
    """Fetch recent news and financial info about the company."""
    queries = [
        f"{ticker} {company_name} stock analysis 2025",
        f"{ticker} earnings revenue financial results",
        f"{ticker} {company_name} analyst recommendation",
    ]
    snippets: list[str] = []
    for query in queries:
        result = tavily.search(query=query, max_results=3, search_depth="advanced")
        for item in result.get("results", []):
            snippets.append(f"[{item['title']}]\n{item['content']}\nSource: {item['url']}")
    return "\n\n---\n\n".join(snippets)


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """You are a professional equity research analyst.
Your job is to analyze publicly available information about a stock and produce a concise investment report.
Always end with a clear recommendation: BUY, HOLD, or SELL, with a short justification.
Write in English. Be objective, cite sources where relevant."""

REPORT_TEMPLATE = """Analyze the following company and produce an investment report.

Company: {company_name}
Ticker: {ticker}
Exchange: {exchange}

## Recent news and data gathered from the web:
{search_results}

## Instructions
1. Summarize the company's business and recent performance.
2. Identify key risks and opportunities.
3. Provide a valuation comment if data is available.
4. Give a final recommendation: **BUY / HOLD / SELL** with a 2-3 sentence rationale.

Structure your report with clear sections:
- Company Overview
- Recent Performance & News
- Key Risks
- Key Opportunities
- Recommendation
"""


def generate_report(ticker: str, company_name: str, exchange: str = "NYSE") -> str:
    tavily = _tavily_client()
    model = _wx_client()

    print(f"[1/3] Searching for information on {ticker}...")
    search_results = search_company(tavily, ticker, company_name)

    prompt = REPORT_TEMPLATE.format(
        company_name=company_name,
        ticker=ticker,
        exchange=exchange,
        search_results=search_results,
    )

    print("[2/3] Generating report with watsonx.ai...")
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt},
    ]
    response = model.chat(messages=messages)
    report_text = response["choices"][0]["message"]["content"]

    print("[3/3] Done.\n")
    return report_text


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Stock report agent (watsonx.ai + Tavily)")
    parser.add_argument("ticker", help="Stock ticker symbol, e.g. AAPL")
    parser.add_argument("company", help="Company name, e.g. 'Apple Inc.'")
    parser.add_argument("--exchange", default="NASDAQ", help="Exchange name (default: NASDAQ)")
    parser.add_argument("--output", help="Optional path to save the report as a .txt file")
    args = parser.parse_args()

    report = generate_report(
        ticker=args.ticker.upper(),
        company_name=args.company,
        exchange=args.exchange,
    )

    print("=" * 70)
    print(report)
    print("=" * 70)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"\nReport saved to {args.output}")


if __name__ == "__main__":
    main()
