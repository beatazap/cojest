# Programowanie II - Lab 5

**Legenda**

📖 - proszę przeczytać

📝 - warte zapamiętania / zanotowania

⚠️ - zwróć uwagę

✏️ - zadanie do wykonania

🔍 - poszukaj w internecie

## Klasy (przypomnienie z lab2)

Klasa to zdefiniowany zbiór atrybutów i funkcji (metod). Nowy obiekt stworzony z danej klasy nazywamy **instancją**. Interakcja z pozostałymi obiektami odbywa się przez wcześniej zdefiniowane metody.

#### minimalna definicja klasy
Aby zdefiniować klasę należy użyć słowa kluczowego `class`, dowolną nazwę (najlepiej zaczynającą się z dużej litery) oraz dwukropek.
```python
class NazwaKlasy:
    pass
```

Słowo kluczowe `pass` odgrywa tutaj kluczową rolę, w Pythonie nie ma możliwości pozostawienia pustej definicji klasy/funkcji oraz bloku instrukcji sterowania.

#### Tworzenie instacji z klasy

Przykład:
```python
# Definicja klasy
class Backpack:
    pass
    
arnolds_backpack = Backpack()  # nowa instancja przypisana do zmiennej arnolds_backpack
jimmys_backpack = Backpack()  # kolejna instancja tym razem przypisana do zmiennej jimmys_backpack
```

#### Atrybuty
Atrybutami nazywamy zmienne zdefiniowane w klasie.

Przykład 1:
```python
class Backpack:
    color = None

arnolds_backpack = Backpack()
arnolds_backpack.color = 'Blue'

jimmys_backpack = Backpack()
jimmys_backpack.color = 'Orange'

print(f"Kolor plecaka Jimmiego to {jimmys_backpack.color}")
print(f"Kolor plecaka Arnolda to {arnolds_backpack.color}")
```

Przykład 2:
```python
class Notebook:
    paper_size = 'b4'  # atrybut dostępny dla wszystkich instancji klasy Notebook z domyślną wartością. 
    
    def __init__(self, subject):
        self.subject = subject

arnolds_notebook = Notebook('Matematyka')
jimmys_notebook = Notebook('Fizyka')

print(f"Zeszyt Arnolda formatu {arnolds_notebook.paper_size} służy mu do przedmiotu {arnolds_notebook.subject}")
print(f"Zeszyt Jimmiego formatu {jimmys_notebook.paper_size} służy mu do przedmiotu {jimmys_notebook.subject}")
```

Przykład 3:

Modyfikacja atrybutu `paper_size` ma wpływ tylko na konkretną instancję.
```python
class Notebook:
    paper_size = 'B4'  # atrybut dostępny dla wszystkich instancji klasy Notebook z domyślną wartością. 
    
    def __init__(self, subject):
        self.subject = subject

arnolds_notebook = Notebook('Matematyka')
arnolds_notebook.paper_size = 'A5'

jimmys_notebook = Notebook('Fizyka')

print(f"Zeszyt Arnolda formatu {arnolds_notebook.paper_size} służy mu do przedmiotu {arnolds_notebook.subject}")
print(f"Zeszyt Jimmiego formatu {jimmys_notebook.paper_size} służy mu do przedmiotu {jimmys_notebook.subject}")
```

## Metody statyczne 



## Dziedziczenie

### Polimorfizm
