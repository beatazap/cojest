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
__Utwórz środowisko__
Przed przystąpieniem do wykonywania zadań utwórz nowe środowisko w którym zainstalujesz następujące moduły:
```
Flask
Flask-SQLAlchemy
SQLAlchemy
```

__Minimalna aplikacja__
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

#### Obsługa Bazy Danych
Do Obsługi bazy danych możemy wykorzystać popularny silnik ORM ([Object–relational mapping](https://pl.wikipedia.org/wiki/Mapowanie_obiektowo-relacyjne)).

Przykład (fragment):
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////./studenci.sqlite3'
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Student %r>' % self.username
```
Do stworzenia pustej bazy danych potrzebujemy uruchomić `flask shell` a następnie zimportować naszą aplikację i wywołać `db.create_all()`.

```python
>>> from app import db
>>> db.create_all()
```

✏️ Stwórz endpoint dla `Student` obsługujący metodę PUT lub POST w celu dodania danych przekazanych w `request.get_json()`.


### Wysyłanie odpowiedzi w formacie JSON
W celu sformatowania obiektu z Pythona na obiekt typu JSON należy wywołać funkcję jsonify z modułu flask

Przykład (fragment):
```python
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'msg': 'Witaj Świecie!'})
        
@app.route('/square/<int:value>', methods = ['GET'])
def square(value):
    return jsonify({'square_root': value**2})
```

✏️ Stwórz endpoint dla `Student` obsługujący metodę GET który zwróci listę wszystkich studentów w bazie danych.

W Przypadku bardziej skomplikowanych modeli warto skorzystać z modułu `Marshmallow` który pozwala nam określić schemat modelu.

🔍 Poszukaj informacji na temat modułu `Marshmallow`.


### Testowanie 
Jednym z narzędzi pozwalającym na przetestowanie endpointów jest [Postman](https://www.postman.com/).

✏️ Zainstaluj narzędzie Postman i użyj go do wywołania dowolnego endpointu.

## Zasoby
* https://beeceptor.com/ - Tworzenie sztucznego API.
* https://dummyapi.io/ - Tworzenie sztucznego API.
* https://flask.palletsprojects.com/en/2.0.x/api/ - Dokumentacja dla Flask'a.
* https://flask-sqlalchemy.palletsprojects.com/en/2.x/ - Moduł pozwalający na integracje Flask z silnikiem do obsługi bazy danych przy pomocy SQLAlchemy.
* https://flask-marshmallow.readthedocs.io/en/latest/ - Moduł do serializacji i deserializacji danych.
