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
