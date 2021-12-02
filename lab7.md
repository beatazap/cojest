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


#### Uprawnienia

Bot posiada szereg uprawnień pozwalających na obsługę dodatkowych akcji, np. wyrzucenie użytkownika za karę z kanału za spamowanie.

![image](https://user-images.githubusercontent.com/77734214/144453891-1166e4b6-1855-417b-b135-63509ea6db13.png)



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

### Bot z grą w zgadywanie

```python
import os
import random
import discord
import asyncio

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$guess'):
            await message.channel.send('Guess a number between 1 and 10.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send('Sorry, you took too long it was {}.'.format(answer))

            if int(guess.content) == answer:
                await message.channel.send('You are right!')
            else:
                await message.channel.send('Oops. It is actually {}.'.format(answer))

```
Źródło: https://github.com/Rapptz/discord.py/blob/v1.7.3/examples/guessing_game.py

### Bot z zadaniem w tle

```python
import discord
import asyncio

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Utwórz i uruchom zadanie w tle
        self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def my_background_task(self):
        await self.wait_until_ready()
        counter = 0
        channel = self.get_channel(1234567) # ID kanału
        while not self.is_closed():
            counter += 1
            await channel.send(counter)
            await asyncio.sleep(60) # Zadanie jest wykonywane co 60 sekund
```

# Bot witający nowego członka
Ten przykład wymaga włączenia uprawnień do `members`.

![image](https://user-images.githubusercontent.com/77734214/144452561-54fe7595-1fc5-44aa-9fd5-e985d7b26fe3.png)

Kod:

```python
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run('token')
```

Źródło: https://github.com/Rapptz/discord.py/blob/v1.7.3/examples/new_member.py

### Uruchomienie
Aby uruchomić bota (jeżeli plik nazywa się `bot.py`) wystarczy wpisać `python bot.py` w konsoli.
