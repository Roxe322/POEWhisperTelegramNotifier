import json
import time
from urllib import request

from config import LOG_PATH, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"


def prepare_telegram_message(message):
    """Remove unnecessary information from the message and apply formatting."""
    split_message = message.split()
    try:
        if "[INFO Client" in message:
            # from 2 to 7 there are debug log information that we don't want to see
            del split_message[2:7]
    except IndexError:
        # Could be any other message, not only the whisper
        pass
    return " ".join(split_message).replace("@From", "From")  # Just to look better


def follow(file):
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


def make_data_to_send(message):
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    json_data = json.dumps(data)

    return json_data.encode("utf-8")


def send_to_telegram(message):
    """Send a message to a Telegram chat."""
    message_text = prepare_telegram_message(message)
    data = make_data_to_send(message_text)
    req = request.Request(API_URL, data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    try:
        request.urlopen(req)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    send_to_telegram("Started to follow the log file for your whispers")
    try:
        with open(LOG_PATH, encoding="utf-8") as logfile:
            log_lines = follow(logfile)
            for log_line in log_lines:
                print(log_line)
                if "@From" in log_line:
                    send_to_telegram(log_line)
    except FileNotFoundError:
        send_to_telegram(
            "Log file not found at provided path, please check the path and restart the script"
        )
    except KeyboardInterrupt:
        send_to_telegram(
            "Stopped following the log file because of the keyboard interrupt, please restart the script"
        )
    except Exception as e:
        print(e)
        send_to_telegram(
            f"Stopped following the log file because of the error: {e}, please restart the script"
        )
