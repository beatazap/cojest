# Programowanie II - Lab 11

**Legenda**

📖 - proszę przeczytać

📝 - warte zapamiętania / zanotowania

⚠️ - zwróć uwagę

✏️ - zadanie do wykonania

🔍 - poszukaj w internecie

# Wprowadzenie do Architektury REST API

## REST
REST (Representational State Transfer) zestaw reguł opisujących dostęp do danych. 

Głównymi cechami architektury są:
* Klient – Serwer w których istnieje granica która rozdziela kto jest kim.
* Bezstanowość - określa, że indywidualne zapytanie do serwera posiada wystarczającą ilość informacji do obsłużenia tego zapytania.
* Pamięć podręczna może zostać wykorzystana w celu zwiększenia wydajności.
* system zbudowany na warstwach pozwala połączyć klienta z dowolnym serwerem do obsługi jego zapytania. 
* Ujednolicony interfejs.

### Standardowe metody
Metody HTTP są standardowymi metodami komunikacji w architekturze REST.

| nazwa metody | opis |
| -------------|------|
| GET | Żądanie pobrania zasobu z serwera |
| POST | Żądanie obsłużenia zapytania (wraz z załączonymi danymi) przez dany zasób |
| PUT | Utworzenie lub aktualizacja stanu danego zasobu na podstawie żądania |
| DELETE | Żądanie usunięcia danego zasobu |

### Minimalna aplikacja Flask
```python
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Hello World from FLASK"
if __name__ == '__main__':
    app.run(debug=True)     
```

#### Dodawanie nowych endpointów
Endpoint to nic innego jak ścieżka którą podajemy w pasku URL. Główną ścieżką kiedy wywołamy adres naszej strony (serwera) jest `/`. 

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Witaj na stronie głównej"
    
@app.route('/hello')
def say_hello():
    return "Cześć!"
    
if __name__ == '__main__':
    app.run(debug=True)     
```

W ścieżce możemy również umieścić parametry które następnie zostaną przekazane do funkcji zajmującej się obsługą danego żądania.

Przykład (fragment):
 ```python
@app.route('/hello/<str:name>')
def say_hello_to(name):
    return f"Cześć {name}!"
```  

✏️ Dodaj do aplikacji Flask nowy endpoint który posłuży do policzenia sumy kwadratów dwóch liczb przekazanych w adresie URL.


#### Obsługa metod
Flask pozwala nam na dostęp do aktulnej metody HTTP przy pomocy `request`. Specjalnej zmiennej przechowującej stan aktualnego żądania.
Musimy również przekazać do `@app.route` listę method które chcemy obsłużyć na przykład: `methods = ['GET', 'POSTS']`.

Przykład:
```python
from flask import Flask, request
app = Flask(__name__)
@app.route('/', methods = ['GET', 'POSTS'])
def home():
    if request.method == 'GET':
        return "Hello World z FLASKa"
    elif request.method == 'POST':
        return "Coś do mnie wysyłasz :)"
    else:
        return "coś nie tak :("
        
if __name__ == '__main__':
    app.run(debug=True)     
```

✏️ Dodaj do aplikacji Flask nowy endpoint dla każdej metody.

#### 


### Testowanie 
Jednym z narzędzi pozwalającym na przetestowanie endpointów jest [Postman](https://www.postman.com/).

✏️ Zainstaluj narzędzie Postman i użyj go do wywołania dowolnego endpointu.

## Zasoby
* https://beeceptor.com/ - Tworzenie sztucznego API
* https://dummyapi.io/ - Tworzenie sztucznego API
