# Programowanie II - Lab 3

**Legenda**

馃摉 - prosz臋 przeczyta膰

馃摑 - warte zapami臋tania / zanotowania

鈿狅笍 - zwr贸膰 uwag臋

鉁忥笍 - zadanie do wykonania

馃攳 - poszukaj w internecie

## Zadanie

Stw贸rz skrypt do obs艂ugi Banku.

Skrypt powinien implementowa膰 nast臋puj膮ce klasy:

* `Bank` - do przechowywania informacji o kontach bankowych (klasa Account), oraz nazwy banku.
* `Account` - do przechowywania informacji o u偶ytkowniku konta np. imi臋 i nazwisko, numer konta bankowego (powinien by膰 unikalny), oraz saldo.
* `WireTransfer` - do przechowywania informacji o przelewach np. identyfikator porz膮dkowy dla ca艂ego banku, z jakiego numeru konta, na jaki numer konta i kwota na jak膮 zosta艂 dokonany przelew.

**Przyk艂ad do u偶ycia:**

Zaimplementuj:

* Klasa `Bank` powinna implementowa膰 metod臋 `deposit` kt贸ra b臋dzie wylicza膰 sum臋 wszystkich depozyt贸w jakie znajduj膮 si臋 na kontach klient贸w.
* Klasa `Account` powinna posiada膰 histori臋 przelew贸w z/na konto.
* Klasa `Account` powinna implementowa膰 metod臋 `verify_balance` kt贸ra sprawdzi czy kwota na koncie zgadza si臋 z sum膮 przelew贸w z/na konta.

鈿狅笍 Klasy mog膮 potrzebowa膰 jeszcze dodatkowych atrybut贸w i funkcji - zastan贸w si臋 jakie.
