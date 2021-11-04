# Programowanie II - Lab 4

**Legenda**

📖 - proszę przeczytać

📝 - warte zapamiętania / zanotowania

⚠️ - zwróć uwagę

✏️ - zadanie do wykonania

🔍 - poszukaj w internecie

## Obiekt
Obiekt jest abstrakcyjną strukturą danych, która posiada swój unikalny ID, typ oraz wartość. Typ obiektu jest określany dynamicznie na podstawie tego jakie metody udostępnia, technika ta jest nazywana 📖 [duck typing](https://pl.wikipedia.org/wiki/Duck_typing). Dzięki tej technice można ograniczyć wykorzystanie techniki dziedziczenia, gdyż obiekty wykorzystują odpowiednie specjalne metody do budowania zależności między nimi. 

Przykład:
```python
class Dog:
    def make_noice(self):
        print("Making dog noices.")
    
class Cat:
    def make_noice(self):
        print("Making cat noices.")
        

def make_noice(obj):
    obj.make_noice()
    
d = Dog()
c = Cat()

make_noice(d)
make_noice(c)
```

📖 Proszę przeczytać https://docs.python.org/3.9/reference/datamodel.html aby dowiedzieć się więcej.

## Magiczne Metody
Metody specjalne potocznie nazywanej "magicznymi metodami". 
