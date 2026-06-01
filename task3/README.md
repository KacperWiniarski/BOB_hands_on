# Task 3: Testowanie Aplikacji - Testy Jednostkowe i Integracyjne

Celem tego zadania jest wykorzystanie BOB'a do stworzenia kompleksowego zestawu testów dla agenta AI, zapewniającego niezawodność i poprawność działania aplikacji.

## Cel ćwiczenia

Nauczysz się, jak efektywnie wykorzystać BOB'a do:
- Tworzenia testów jednostkowych (unit tests)
- Implementacji testów integracyjnych
- Mockowania zewnętrznych zależności (API)
- Organizacji struktury testów
- Zapewnienia wysokiego pokrycia kodu testami

## Wymagania wstępne

Upewnij się, że masz zainstalowane:
```bash
pip install pytest pytest-mock pytest-cov
```

## Instrukcje

### Krok 1: Zlecenie stworzenia testów BOB'owi

Skopiuj i wklej poniższy prompt do BOB'a:

```
Stwórz kompleksowy zestaw testów dla aplikacji agent.py. Potrzebuję:

1. **Strukturę testów**: 
   - Utwórz katalog `tests/` z odpowiednią strukturą
   - Dodaj plik `__init__.py`
   - Stwórz osobne pliki testowe dla różnych komponentów

2. **Testy jednostkowe** dla:
   - Funkcji `_wx_client()` - testuj poprawność inicjalizacji klienta watsonx.ai
   - Funkcji `_tavily_client()` - testuj poprawność inicjalizacji klienta Tavily
   - Funkcji `search_company()` - testuj przetwarzanie wyników wyszukiwania
   - Funkcji `generate_report()` - testuj generowanie raportu

3. **Mockowanie zależności**:
   - Mockuj wywołania API do IBM watsonx.ai
   - Mockuj wywołania API do Tavily
   - Mockuj zmienne środowiskowe
   - Użyj pytest-mock do tworzenia mocków

4. **Testy integracyjne**:
   - Test end-to-end dla całego procesu generowania raportu
   - Test obsługi błędów (brak kluczy API, błędy sieci, itp.)

5. **Testy walidacji danych**:
   - Test poprawności formatowania tickera
   - Test obsługi różnych formatów danych wejściowych
   - Test walidacji parametrów

6. **Fixtures**:
   - Stwórz fixtures dla przykładowych danych (mock responses)
   - Fixtures dla konfiguracji testowej

7. **Konfiguracja pytest**:
   - Dodaj plik `pytest.ini` lub `pyproject.toml` z konfiguracją
   - Skonfiguruj pokrycie kodu (coverage)

Dla każdego testu:
- Użyj jasnych, opisowych nazw
- Dodaj docstringi wyjaśniające, co test sprawdza
- Zastosuj pattern Arrange-Act-Assert
- Uwzględnij przypadki brzegowe (edge cases)

Dodatkowo:
- Dodaj plik `conftest.py` z współdzielonymi fixtures
- Stwórz przykładowe dane testowe w osobnym pliku
- Dodaj README.md w katalogu tests/ z instrukcjami uruchamiania testów
```

### Krok 2: Uruchomienie testów

Po stworzeniu testów przez BOB'a, uruchom je:

```bash
# Uruchom wszystkie testy
pytest

# Uruchom z szczegółowym outputem
pytest -v

# Uruchom z pokryciem kodu
pytest --cov=. --cov-report=html

# Uruchom konkretny plik testowy
pytest tests/test_agent.py

# Uruchom konkretny test
pytest tests/test_agent.py::test_search_company
```

### Krok 3: Analiza wyników

Sprawdź:
- Czy wszystkie testy przechodzą ✅
- Jaki jest procent pokrycia kodu
- Czy są jakieś ostrzeżenia lub błędy
- Raport pokrycia w `htmlcov/index.html`

### Krok 4: Iteracja i poprawa

Jeśli testy nie przechodzą lub pokrycie jest niskie, możesz poprosić BOB'a:

```
Testy nie przechodzą z powodu [opisz błąd]. Czy możesz to naprawić?
```

lub

```
Pokrycie kodu wynosi tylko 60%. Dodaj testy dla nieprzetestowanych części kodu.
```

## Przykładowe pytania uzupełniające

- "Dodaj testy dla obsługi timeout'ów w wywołaniach API"
- "Stwórz testy parametryzowane dla różnych tickerów"
- "Jak mogę przetestować funkcję main() z różnymi argumentami CLI?"
- "Dodaj testy dla przypadków, gdy API zwraca puste wyniki"
- "Stwórz testy wydajnościowe sprawdzające czas wykonania"

## Struktura testów (przykład)

```
tests/
├── __init__.py
├── conftest.py              # Współdzielone fixtures
├── test_agent.py            # Testy głównej logiki
├── test_clients.py          # Testy inicjalizacji klientów
├── test_search.py           # Testy funkcji wyszukiwania
├── test_integration.py      # Testy integracyjne
├── fixtures/
│   ├── mock_responses.py    # Przykładowe odpowiedzi API
│   └── test_data.py         # Dane testowe
└── README.md                # Instrukcje testowania
```

## Oczekiwane rezultaty

Po zakończeniu tego zadania powinieneś mieć:
- ✅ Kompletny zestaw testów jednostkowych
- ✅ Testy integracyjne sprawdzające cały flow
- ✅ Pokrycie kodu na poziomie minimum 80%
- ✅ Dokumentację testów
- ✅ Automatyczne wykrywanie regresji
- ✅ Pewność, że kod działa poprawnie

## Wskazówki

- **Mockuj zewnętrzne API**: Nigdy nie wywołuj prawdziwych API w testach jednostkowych
- **Testuj przypadki brzegowe**: Puste stringi, None, błędne formaty
- **Używaj fixtures**: Unikaj duplikacji kodu testowego
- **Testy powinny być szybkie**: Wszystkie testy powinny wykonać się w kilka sekund
- **Jeden test = jedna rzecz**: Każdy test powinien sprawdzać jedną konkretną funkcjonalność
- **Testy powinny być niezależne**: Kolejność wykonania nie powinna mieć znaczenia

## Continuous Integration (opcjonalnie)

Możesz poprosić BOB'a o dodanie konfiguracji CI/CD:

```
Dodaj konfigurację GitHub Actions, która automatycznie uruchomi testy przy każdym push'u i pull request'cie.
```

## Następne kroki

Po zakończeniu testowania i osiągnięciu zadowalającego pokrycia kodu, przejdź do Task 4, gdzie będziesz rozszerzać funkcjonalność agenta o nowe features.