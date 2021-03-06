# Programowanie II - Lab 6

**Legenda**

馃摉 - prosz臋 przeczyta膰

馃摑 - warte zapami臋tania / zanotowania

鈿狅笍 - zwr贸膰 uwag臋

鉁忥笍 - zadanie do wykonania

馃攳 - poszukaj w internecie

# 艢rodowiska wirtualne
艢rodowiskiem wirtualnym w pythonie nazywamy odseparowane od siebie instancje pythona - okrojone kopie 艣rodowiska bazowego. 
Pozwala nam to na r贸wnocze艣n膮 wsp贸艂prac臋 nad r贸偶nymi pod wzgl臋dem modu艂贸w i wersji projektami. 

Dzi臋ki zastosowaniu wirtualnych 艣rodowisk jeste艣my w stanie ograniczy膰 problem z zale偶no艣ciami bibliotek kt贸re mog膮 uniemo偶liwi膰 nam uruchomienie naszego skryptu b膮d藕 programu. Problem ten uzyska艂 nawet w艂asn膮 nazw臋 ["Piek艂o zale偶no艣ci"](https://pl.wikipedia.org/wiki/Piek%C5%82o_zale%C5%BCno%C5%9Bci).

Do zarz膮dzania pakietami wykorzystujemy narz臋dzie `pip`, kt贸re jest dostarczane wraz z instalacj膮 python'a.

### :memo: Lista przydatnych komend

lista zainstalowanych modu艂贸w:
```bash
pip list
```
lista zainstalowanych modu艂贸w w sk艂adni dla komendy `pip install -r`.
```bash
pip freeze > requirements.txt  # zapisujemy informacj臋 zainstalowanych modu艂ach do pliku requirements.txt
```

instalacja nowego modu艂u:
```bash
pip install [--user] [-U] nazwa_pakietu[==konkretna wersja]
pip install -r requirements.txt   # instalujemy list臋 pakiet贸w kt贸re znajduj膮 si臋 w pliku requirements.txt
```

Usuni臋cie modu艂u z 艣rodowiska:
```bash
pip uninstall nazwa_pakietu
pip uninstall -r requirements.txt  # usunie list臋 pakiet贸w kt贸re znajduj膮 si臋 w pliku requirements.txt
```

## Tworzenie przy pomocy modu艂u venv
Aby utworzy膰 nowe 艣rodowisko nale偶y u偶y膰 modu艂u `venv`, kt贸ry jest integraln膮 cz臋艣ci膮 pythona 3.X.

### Tworzenie nowego 艣rodowiska
Do stworzenia nowego 艣rodowiska wykorzystujemy nast臋puj膮c膮 komend臋:
```cmd
python -m venv venv
```
### Aktywacja 艣rodowiska
W systemie linux/macos:
```cmd
venv/bin/activate
```

W systemie Windows:
```cmd
venv/Scripts/activate
```

## Zarz膮dzanie
Istniej膮 r贸wnie偶 inne narz臋dzia do zarz膮dzania wirtualnymi 艣rodowiskami takie jak `pipenv`, `virtualenv`, `conda`.

馃摉 Prosz臋 przeczyta膰 https://github.com/pypa/pipenv.

馃摉 Prosz臋 przeczyta膰 https://virtualenv.pypa.io/en/latest/.

馃摉 Prosz臋 przeczyta膰 https://docs.python.org/3.9/tutorial/venv.html.

馃摉 Prosz臋 przeczyta膰 https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

## Zadania

鉁忥笍 Znajd藕 na internecie (na githubie) dowolne repozytorium kodu w Pythonie i spr贸buj stworzy膰 艣rodowisko potrzebne do jego developmentu.

鉁忥笍 Utw贸rz nowe 艣rodowisko w kt贸rym zainstalujesz biblioteki: 
 * `ipython`
 * `pandas`
 * `numpy`
 * `matplotlib`
 * `plotly`
 * `streamlit`
 * `opencv-python`
 * `tensorflow`

U偶yj w tym celu narz臋dzia `pip`.

鉁忥笍 Wyekportuj zainstalowane biblioteki w nowo utworzonym 艣rodwisku do pliku `requirements.txt`.

鉁忥笍 Utw贸rz kolejne 艣rodowisko tym razem z wykorzystaniem pliku `requirements.txt`.

鉁忥笍 Utw贸rz nowe 艣rodowisko w kt贸rym zainstalujesz https://github.com/jazzband/pip-tools. U偶yj narz臋dzi `pip-compile` i `pip-sync` (馃攳 sprawd藕 dokumentacje na stronie) do zbudowania 艣rodowiska na potrzeby NLP (Natural Language Processing) zawieraj膮cego nast臋puj膮ce biblioteki:

* `ipython`
* `jupyter`
* `scikit-learn`
* `matplotlib`

鉁忥笍 Jaka jest r贸偶nica mi臋dzy narz臋dziami `pip` a `pip-tools`? Kt贸ry Twoim zdaniem jest lepszy?
