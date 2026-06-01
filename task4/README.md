# Task 4: Custom Mode i Frontend - Rozszerzenie Funkcjonalności

Celem tego zadania jest nauczenie się tworzenia własnych trybów (custom modes) w BOB'ie oraz wykorzystanie ich do stworzenia interfejsu webowego dla agenta AI.

## Cel ćwiczenia

Nauczysz się:
- Jak tworzyć i konfigurować custom modes w BOB'ie
- Jak przełączać się między różnymi trybami
- Jak wykorzystać specjalistyczny tryb do tworzenia frontendu
- Jak zintegrować frontend z backendem agenta AI

## Część 1: Tworzenie Custom Mode

### Krok 1: Zrozumienie Custom Modes

Custom modes w BOB'ie pozwalają na:
- Specjalizację BOB'a w konkretnych zadaniach
- Dostęp do dodatkowych narzędzi (np. MCP - Model Context Protocol)
- Optymalizację promptów dla specyficznych przypadków użycia
- Lepszą organizację pracy nad różnymi aspektami projektu

### Krok 2: Utworzenie Custom Mode dla Frontend Development

Skopiuj i wklej poniższy prompt do BOB'a:

```
Chcę stworzyć custom mode o nazwie "Frontend Developer" do tworzenia interfejsów webowych. 

Tryb powinien:
1. Specjalizować się w HTML, CSS, JavaScript i frameworkach frontendowych
2. Mieć dostęp do narzędzi do pracy z plikami statycznymi
3. Być zoptymalizowany do tworzenia responsywnych interfejsów użytkownika
4. Pomagać w integracji z API backendu

Proszę:
- Wyjaśnij, jak mogę utworzyć taki custom mode
- Podaj przykładową konfigurację
- Pomóż mi przełączyć się do tego trybu, gdy będzie gotowy
```

### Krok 3: Aktywacja Custom Mode

Po utworzeniu custom mode, BOB powinien zaproponować przełączenie się do niego. Możesz też ręcznie przełączyć się używając komendy switch_mode.

## Część 2: Tworzenie Frontendu

### Krok 4: Zlecenie stworzenia interfejsu webowego

Po przełączeniu się do trybu Frontend Developer, użyj poniższego promptu:

```
Stwórz nowoczesny interfejs webowy dla agenta analizy akcji. Frontend powinien zawierać:

## Wymagania funkcjonalne:
1. **Formularz wejściowy**:
   - Pole na ticker akcji (np. AAPL)
   - Pole na nazwę firmy (np. Apple Inc.)
   - Pole na giełdę (domyślnie NASDAQ)
   - Przycisk "Generuj Raport"

2. **Wyświetlanie wyników**:
   - Sekcja na wygenerowany raport
   - Podświetlanie rekomendacji (BUY/HOLD/SELL) z kolorami
   - Formatowanie raportu z wyraźnymi sekcjami
   - Loader podczas generowania raportu

3. **Historia**:
   - Lista ostatnio wygenerowanych raportów
   - Możliwość ponownego wyświetlenia poprzednich raportów

## Wymagania techniczne:
1. **Stack technologiczny**:
   - HTML5 z semantycznymi tagami
   - CSS3 z Flexbox/Grid
   - Vanilla JavaScript (lub React, jeśli preferujesz)
   - Fetch API do komunikacji z backendem

2. **Design**:
   - Nowoczesny, czysty interfejs
   - Responsywny design (mobile-first)
   - Ciemny motyw (dark mode)
   - Animacje i transitions dla lepszego UX

3. **Backend Integration**:
   - Endpoint API: POST /api/analyze
   - Request body: {ticker, company, exchange}
   - Response: {report, recommendation, timestamp}

4. **Struktura plików**:
   ```
   frontend/
   ├── index.html
   ├── css/
   │   ├── style.css
   │   └── responsive.css
   ├── js/
   │   ├── app.js
   │   └── api.js
   └── assets/
       └── (ikony, obrazy)
   ```

5. **Dodatkowe funkcje**:
   - Walidacja formularza
   - Obsługa błędów (brak połączenia, błędy API)
   - Loading states
   - Toast notifications dla komunikatów
   - Export raportu do PDF (opcjonalnie)

Stwórz kompletny, działający frontend z wszystkimi plikami.
```

### Krok 5: Tworzenie Backend API (opcjonalnie)

Jeśli chcesz stworzyć prosty backend API dla frontendu, użyj promptu:

```
Stwórz prosty backend API używając Flask, który:
1. Udostępnia endpoint POST /api/analyze
2. Przyjmuje dane z formularza (ticker, company, exchange)
3. Wywołuje funkcję generate_report() z agent.py
4. Zwraca JSON z raportem
5. Obsługuje CORS dla frontendu
6. Ma obsługę błędów i walidację danych

Dodaj również:
- Endpoint GET /api/health do sprawdzania statusu
- Endpoint GET /api/history do pobierania historii raportów
- Zapisywanie raportów do pliku JSON jako prostą bazę danych
```

## Część 3: Testowanie i Integracja

### Krok 6: Uruchomienie aplikacji

1. **Uruchom backend** (jeśli został stworzony):
```bash
python backend/app.py
```

2. **Otwórz frontend**:
```bash
# Prosty serwer HTTP
python -m http.server 8000 -d frontend
```

3. **Otwórz w przeglądarce**:
```
http://localhost:8000
```

### Krok 7: Testowanie funkcjonalności

Przetestuj:
- ✅ Wypełnienie formularza i wysłanie
- ✅ Wyświetlanie loadera podczas generowania
- ✅ Poprawne wyświetlanie raportu
- ✅ Kolorowanie rekomendacji
- ✅ Responsywność na różnych urządzeniach
- ✅ Obsługę błędów
- ✅ Historię raportów

## Przykładowe pytania uzupełniające

Po stworzeniu podstawowego frontendu możesz poprosić BOB'a o:

- "Dodaj wykres cen akcji używając Chart.js"
- "Zaimplementuj dark/light mode toggle"
- "Dodaj animacje przy ładowaniu raportu"
- "Stwórz komponent do porównywania wielu akcji"
- "Dodaj eksport raportu do PDF"
- "Zaimplementuj cache dla raportów w localStorage"
- "Dodaj autouzupełnianie dla tickerów akcji"

## Przełączanie między trybami

Możesz przełączać się między trybami w zależności od potrzeb:

```
Przełącz się do trybu Code - muszę poprawić backend
```

```
Przełącz się do trybu Frontend Developer - chcę dodać nową funkcję do UI
```

## Oczekiwane rezultaty

Po zakończeniu tego zadania powinieneś mieć:
- ✅ Działający custom mode dla frontend development
- ✅ Kompletny interfejs webowy dla agenta AI
- ✅ Integrację frontend-backend
- ✅ Responsywny, nowoczesny design
- ✅ Pełną funkcjonalność generowania i wyświetlania raportów
- ✅ Zrozumienie, jak wykorzystywać różne tryby BOB'a

## Wskazówki

- **Custom modes są potężne**: Wykorzystuj je do specjalizacji BOB'a
- **Przełączaj tryby świadomie**: Każdy tryb ma swoje mocne strony
- **Iteruj**: Najpierw stwórz MVP, potem dodawaj funkcje
- **Testuj na bieżąco**: Sprawdzaj każdą nową funkcję zaraz po dodaniu
- **Pytaj o best practices**: BOB zna najlepsze praktyki dla każdej technologii

## Zaawansowane opcje

### MCP (Model Context Protocol)

W trybie Advance możesz wykorzystać MCP do:
- Integracji z zewnętrznymi narzędziami
- Dostępu do dodatkowych źródeł danych
- Rozszerzenia możliwości BOB'a

Aby przełączyć się do trybu Advance:
```
Przełącz się do trybu Advance - potrzebuję dostępu do MCP
```

## Następne kroki

Po zakończeniu tworzenia frontendu, przejdź do Task 5, gdzie będziesz pracować nad deployment'em i optymalizacją całej aplikacji.