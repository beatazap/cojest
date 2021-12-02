# Programowanie II - Lab 7

**Legenda**

📖 - proszę przeczytać

📝 - warte zapamiętania / zanotowania

⚠️ - zwróć uwagę

✏️ - zadanie do wykonania

🔍 - poszukaj w internecie

# Zaawansowane Biblioteki
## Prosty Discord Bot
Na podstawie dokumentacji https://discordpy.readthedocs.io/en/stable/intro.html.

### Wymagania
Do działania modułu `discord.py` potrzebujemy Python w wersji minimum 3.5

### Wirtualne środowisko 
Utwórzmy środowisko dla naszego projektu:

```shell
python3 -m venv bot-env
```
Aktywacja środowiska:

**Linux**:

```shell
source bot-env/bin/activate
```

**Windows**:

```shell
source bot-env\Scripts\activate.bat
```

Instalacja modułu:
```shell
pip install -U discord.py
```

### Programowanie sterowane zdarzeniami
Programowanie sterowane zdarzeniami opiera się na oczekiwaniu programu na wystąpienie jakiegoś zdarzenia 🙄 a następnie kiedy dane zdarzenie wystąpi, zostaje wywołana odpowiednia akcja przypisana do niego.

📖 Proszę przeczytać [Paradygmaty programowania](https://wazniak.mimuw.edu.pl/index.php?title=Paradygmaty_programowania/Wyk%C5%82ad_15:_Inne_paradygmaty_warte_wspomnienia) aby dowiedzieć się więcej.

### Tworzenie aplikacji
Do uruchomienia naszego Bota wymagany jest klucz zwany tokenem.
Aby go utworzyć należy przejść na stronę https://discord.com/developers/applications.

Krok 1:

Kliknij przycisk \[New Application\]

![image](https://user-images.githubusercontent.com/77734214/144446754-081bf5b5-86ad-445b-bd6d-bbee955859f5.png)

Krok 2:

Podajemy nazwę naszej aplikacji.

![image](https://user-images.githubusercontent.com/77734214/144449651-a5ade611-c763-4ac3-afe4-965fd4f87d7c.png)

Krok 3:

Tworzymy nowego bot'a.

![image](https://user-images.githubusercontent.com/77734214/144450079-e49431b5-8dad-437a-916a-88e7b9b81fc8.png)

Krok 4:

Konfigurujemy go i pobieramy TOKEN.

![image](https://user-images.githubusercontent.com/77734214/144451064-c5491e0c-f4a0-4a0e-b15a-9efc2856bd39.png)


### Minimalna wersja bota

```python
import os
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

if __name__ == '__main__':
    BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    client = MyClient()
    client.run(BOT_TOKEN)
 
```



