# Programowanie II - Lab 10

**Legenda**

馃摉 - prosz臋 przeczyta膰

馃摑 - warte zapami臋tania / zanotowania

鈿狅笍 - zwr贸膰 uwag臋

鉁忥笍 - zadanie do wykonania

馃攳 - poszukaj w internecie

# Zarz膮dzanie projektem 

## Kanban

* Wizualizacja
* Ograniczenie pracy w toku
* Zarz膮dzanie strumieniem

馃摉 Prosz臋 przeczyta膰 https://pl.wikipedia.org/wiki/Kanban

馃摉 Prosz臋 przeczyta膰 https://pl.wikipedia.org/wiki/Kanban_w_tworzeniu_oprogramowania

## Scrum

馃摉 Prosz臋 przeczyta膰 https://pl.wikipedia.org/wiki/Scrum

# Zarz膮dzanie kodem

## Github
GitHub jest platform膮 do hostowania repozytorium kodu przy wykorzystaniu systemu [Git](https://pl.wikipedia.org/wiki/Git_(oprogramowanie)).

馃摑 Link odno艣nie systemu Git https://git-scm.com/.

馃摉 Prosz臋 przeczyta膰 https://git-scm.com/book/en/v2.


### Workflow
Jednym z przyj臋tych standard贸w wsp贸艂pracy mi臋dzy programistami na platformie GitHub (i nie tylko) jest zastosowanie branch'y z g艂贸wnego branch'a `main` do rozwijania osobnych fragment贸w kodu przez r贸偶nych deweloper贸w.

Link do por贸wnania workflow贸w https://www.atlassian.com/git/tutorials/comparing-workflows.

## Zadania

鉁忥笍 Je偶eli jeszcze nie masz konta w serwisie GitHub, utw贸rz je, a nast臋pnie stw贸rz nowe repozytorium w kt贸rym b臋dziesz przechowywa艂 kod z zaj臋膰 z Programowania.

# Tworzenie interfejs贸w graficznych

## TKinter
TK Interface jest domy艣lnie zainstalowanym modu艂em pozwalaj膮cym nam na tworzenie interfejs贸w graficznych.

馃摉 Prosz臋 przeczyta膰 https://docs.python.org/3/library/tkinter.html.

### Klasa Tk
Klasa ``Tk` pozwala nam zdefiniowa膰 nasze okno w spos贸b obiektowy.

```python
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Sample Python GUI Window')
        self.geometry('300x300')

if __name__ == "__main__":
    app = App()
    app.mainloop()  # wywo艂anie p臋tli obs艂uguj膮cej zdarzenia.
    
```        

## Thread
W膮tkiem w programowaniu nazywamy kod kt贸ry wykonuje si臋 r贸wnolegle wzgl臋dem innego kodu wykonywanego w naszym programie. Niestety (albo stety 馃檪), Python symuluje w膮tki, co pozwala na wykonywanie ich w systemach jednoprocesorowych, jak i wieloprocesorowych bez zmiany kodu, co ma to te偶 wp艂yw na obni偶on膮 wydajno艣膰. 

馃摉 Prosz臋 przeczyta膰 https://pl.wikipedia.org/wiki/Global_Interpreter_Lock.

馃摉 Prosz臋 przeczyta膰 https://wazniak.mimuw.edu.pl/images/5/54/Sop_02_wyk_bw_1.1.pdf


w Pythonie modu艂 zajmuj膮cy si臋 wysokopoziomow膮 obs艂ug膮 w膮tk贸w nazywa si臋 `threading`.

馃摉 Prosz臋 przeczyta膰 https://docs.python.org/3.9/library/threading.html

### Tworzenie w膮tku
Nowy w膮tek mo偶na stworzy膰 na dwa sposoby: zdefiniowanie funkcji lub klasy kt贸ra ma zosta膰 uruchomiana. 

Na tych zaj臋ciach om贸wimy drugi spos贸b, czyli z wykorzystaniem klasy `Thread`.

Przyk艂ad:
```python
from threading import Thread

class MinThread(Thread):
    def run(self):
      # Tutaj pojawia si臋 nasz kod kt贸ry chcemy wywo艂a膰.
      pass
      
if __name__ == "__main__":
    thread = minThread()
    thread.run()
    # co艣 tu brakuje ale to zaraz :)
```


Nale偶y pami臋t膮膰, 偶e w膮tek kt贸ry zosta艂 uruchomiony dzia艂a niezale偶nie i zako艅czenie dzia艂ania naszego g艂贸wnego w膮tku (czyli naszego skryptu) nie powoduje automatycznego zako艅czenie w膮tku.

W tym celu musimy wywo艂a膰 metod臋 `join()` klasy `Thread`. kt贸ra poinformuje g艂贸wny w膮tek aby "zaczeka艂" na zako艅czenie wykonywania w膮tku.  

Uzupe艂niony przyk艂ad:
```python
from threading import Thread

class MinThread(Thread):
    def run(self):
      # Tutaj pojawia si臋 nasz kod kt贸ry chcemy wywo艂a膰.
      pass
      
if __name__ == "__main__":
    thread = minThread()
    thread.run()
    print("Hello World")
    thread.join() # <--
```

鉁忥笍 Stw贸rz w膮tek kt贸ry b臋dzie odlicza艂 do 30.

鉁忥笍 Zmodyfikuj uprzednio utworzony kod aby uruchomi膰 dwa w膮tki jednocze艣nie.


## Zadania

鉁忥笍 Stw贸rz Skrypt kt贸re b臋dzie uruchamia膰 dowoln膮 (zdefiniowan膮 przez Ciebie) komend臋/program.

鉁忥笍 Na podstawie uprzednio utworzonego skryptu, stw贸rz GUI kt贸re b臋dzie posiada膰 przycisk wywo艂uj膮cy funkcj臋 uruchamiaj膮c膮 dowoln膮 komend臋/program.

鉁忥笍 Stw贸rz GUI kt贸re b臋dzie posiada膰 przycisk wykonuj膮cy zadanie w w膮tku (np. odliczaj膮cy do 60 sekund z interwa艂em 1 sekunda). Wynik odliczania powinien wy艣wietla膰 si臋 w okienku.
