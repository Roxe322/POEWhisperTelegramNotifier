# POEWhisperTelegramNotifier
Small script which checks your Client.txt log file and sending message to your telegram when someone whispers you.

## Requirements
* [Python 3+](https://wiki.python.org/moin/BeginnersGuide/Download)

## Setup
Open `config.py` file with any text editor and change `LOG_PATH` and `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`. Don't remove quotes.

## How to set config variables:
* `LOG_PATH` - path to your `Client.txt` log file. You can find it in your `Path of Exile` folder. For example: `C:\Program Files (x86)\Grinding Gear Games\Path of Exile\logs\Client.txt` or `F:\Games\Steam\steamapps\common\Path of Exile\logs\client.txt`
* `TELEGRAM_BOT_TOKEN` - you can get it from [@BotFather](https://t.me/BotFather). Just create new bot and copy token.
* `TELEGRAM_CHAT_ID` - you can get it from [@userinfobot](https://t.me/userinfobot). Just send `/start` command and copy `id` field.


## Run
Run `python3 main.py` in terminal / cmd / powershell
