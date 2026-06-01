# Task 2: Przegląd Kodu - Analiza i Usprawnienia

Celem tego zadania jest wykorzystanie BOB'a do przeprowadzenia szczegółowego przeglądu kodu agenta AI i zidentyfikowania potencjalnych usprawnień oraz błędów.

## Cel ćwiczenia

Nauczysz się, jak efektywnie wykorzystać BOB'a do:
- Identyfikacji potencjalnych błędów w kodzie
- Sugerowania usprawnień i optymalizacji
- Wykrywania problemów z bezpieczeństwem
- Poprawy jakości kodu zgodnie z najlepszymi praktykami

## Instrukcje

### Krok 1: Przygotowanie

Upewnij się, że masz otwarty plik `agent.py` w edytorze VS Code.

### Krok 2: Zlecenie przeglądu BOB'owi

Skopiuj i wklej poniższy prompt do BOB'a:

```
Przeanalizuj plik agent.py i wykonaj szczegółowy przegląd kodu. Zidentyfikuj:

1. **Potencjalne błędy**: Wskaż miejsca, które mogą powodować błędy runtime, wyjątki lub nieprawidłowe działanie
2. **Problemy z bezpieczeństwem**: Sprawdź obsługę zmiennych środowiskowych, danych wejściowych użytkownika i potencjalne luki
3. **Usprawnienia wydajności**: Zasugeruj optymalizacje, które mogą poprawić szybkość działania
4. **Jakość kodu**: Oceń czytelność, strukturę i zgodność z PEP 8
5. **Obsługa błędów**: Sprawdź, czy wszystkie potencjalne wyjątki są odpowiednio obsługiwane
6. **Dokumentacja**: Oceń jakość docstringów i komentarzy
7. **Testowanie**: Zasugeruj, jakie testy jednostkowe powinny być dodane

Dla każdego znalezionego problemu:
- Wskaż konkretną linię kodu
- Wyjaśnij, dlaczego to jest problem
- Zaproponuj konkretne rozwiązanie z przykładem kodu

Na koniec przedstaw priorytetową listę zmian (od najważniejszych do najmniej istotnych).
```

### Krok 3: Analiza wyników

BOB przeprowadzi szczegółową analizę i przedstawi:
- Listę znalezionych problemów z opisami
- Konkretne sugestie poprawek
- Przykłady ulepszonego kodu
- Priorytetyzację zmian

### Krok 4: Implementacja poprawek

Na podstawie rekomendacji BOB'a możesz:
1. Poprosić BOB'a o implementację konkretnych zmian
2. Samodzielnie wprowadzić sugerowane poprawki
3. Zadać dodatkowe pytania o szczegóły implementacji

## Przykładowe pytania uzupełniające

Po otrzymaniu pierwszej analizy, możesz zadać BOB'owi dodatkowe pytania:

- "Czy możesz pokazać, jak dodać kompleksową obsługę błędów dla funkcji search_company?"
- "Jak mogę zoptymalizować równoległe wykonywanie zapytań do Tavily?"
- "Zaproponuj strukturę testów jednostkowych dla tego modułu"
- "Jak mogę dodać logowanie do tego kodu?"
- "Czy możesz zrefaktoryzować kod, aby był bardziej modularny?"

## Oczekiwane rezultaty

Po zakończeniu tego zadania powinieneś:
- ✅ Zrozumieć mocne i słabe strony obecnego kodu
- ✅ Mieć listę konkretnych usprawnień do wdrożenia
- ✅ Wiedzieć, jak poprawić bezpieczeństwo i niezawodność kodu
- ✅ Nauczyć się, jak efektywnie komunikować się z BOB'em w kontekście przeglądu kodu

## Wskazówki

- Bądź konkretny w swoich pytaniach do BOB'a
- Proś o przykłady kodu, nie tylko teoretyczne wyjaśnienia
- Jeśli coś jest niejasne, pytaj o szczegóły
- BOB może implementować zmiany za Ciebie - wykorzystaj to!
- Możesz prosić o przegląd konkretnych fragmentów kodu, jeśli nie chcesz analizować całego pliku

## Następne kroki

Po zakończeniu przeglądu i implementacji poprawek, przejdź do Task 3, gdzie będziesz rozszerzać funkcjonalność agenta.