# Task 1: Konfiguracja - Klucze API i Instalacja Wymagań

To zadanie obejmuje początkową konfigurację wymaganą do uruchomienia projektu agenta AI.

## Wymagania wstępne

- Python 3.8 lub wyższy
- pip (instalator pakietów Python)

## Krok 1: Instalacja wymaganych pakietów

Zainstaluj wszystkie niezbędne zależności Python używając pip:

```bash
pip install -r requirements.txt
```

To zainstaluje:
- `ibm-watsonx-ai` - SDK IBM watsonx.ai do integracji z modelami AI
- `tavily-python` - Klient API Tavily do wyszukiwania w internecie
- `python-dotenv` - Zarządzanie zmiennymi środowiskowymi

## Krok 2: Konfiguracja kluczy API

### 2.1 Utworzenie pliku środowiskowego

Skopiuj przykładowy plik środowiskowy, aby utworzyć własną konfigurację:

```bash
cp .env.example .env
```

### 2.2 Pozyskanie kluczy API

Będziesz potrzebować następujących kluczy API:

#### Klucz API IBM watsonx.ai
1. Przejdź do [IBM Cloud](https://cloud.ibm.com/)
2. Utwórz konto lub zaloguj się
3. Przejdź do usługi watsonx.ai
4. Utwórz nowy projekt lub wybierz istniejący
5. Pobierz swój klucz API z panelu IBM Cloud
6. Zanotuj swój Project ID z ustawień projektu

#### Klucz API Tavily
1. Przejdź do [Tavily](https://tavily.com/)
2. Zarejestruj konto
3. Przejdź do swojego panelu
4. Wygeneruj klucz API

### 2.3 Aktualizacja pliku .env

Otwórz plik `.env` i zastąp wartości zastępcze swoimi rzeczywistymi danymi uwierzytelniającymi:

```env
# IBM watsonx.ai
WATSONX_URL=https://eu-de.ml.cloud.ibm.com
WATSONX_APIKEY=twoj_rzeczywisty_klucz_api_ibm
WATSONX_PROJECT_ID=twoj_rzeczywisty_id_projektu
WATSONX_MODEL=meta-llama/llama-3-3-70b-instruct

# Tavily
TAVILY_API_KEY=twoj_rzeczywisty_klucz_api_tavily
```

**Ważne:** Nigdy nie commituj pliku `.env` do kontroli wersji. Zawiera on wrażliwe dane uwierzytelniające.

## Weryfikacja

Aby zweryfikować, czy konfiguracja jest poprawna, możesz uruchomić prosty test:

```bash
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('Konfiguracja OK' if os.getenv('WATSONX_APIKEY') and os.getenv('TAVILY_API_KEY') else 'Brakuje kluczy')"
```

## Rozwiązywanie problemów

### Problemy z instalacją
- Jeśli napotkasz błędy uprawnień, spróbuj użyć `pip install --user -r requirements.txt`
- W systemie Windows może być konieczne użycie `python -m pip install -r requirements.txt`

### Problemy z kluczami API
- Upewnij się, że nie ma dodatkowych spacji ani cudzysłowów wokół kluczy API w pliku `.env`
- Zweryfikuj, czy Twoje klucze API są aktywne i mają niezbędne uprawnienia
- Sprawdź, czy Twój ID projektu IBM watsonx.ai jest poprawny

## Następne kroki

Po zakończeniu konfiguracji możesz przejść do kolejnych zadań, które będą obejmować implementację i testowanie funkcjonalności agenta AI.