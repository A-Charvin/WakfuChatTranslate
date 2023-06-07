import requests
import os
import PySimpleGUI as sg
import time

# Get the username of the current user
username = os.getlogin()

# Wakfu chat log file path
chat_log_file = f'C:/Users/{username}/AppData/Roaming/zaap/wakfu/logs/wakfu_chat.log'

# Google Translate API endpoint
translate_api_endpoint = 'https://translate.googleapis.com/translate_a/single'

# Default translation settings
from_lang = 'auto'
to_lang = 'en'

# GUI setup
sg.theme("DarkTeal9")  # Set the window theme to a dark theme

layout = [[sg.Multiline(size=(80, 20), key="-OUTPUT-")]]
window = sg.Window("Wakfu Chat Translator", layout, finalize=True)

def translate_message(message):
    # Build the translation API query
    query_params = {
        'client': 'gtx',
        'sl': from_lang,
        'tl': to_lang,
        'dt': 't',
        'q': message,
    }
    response = requests.get(translate_api_endpoint, params=query_params)

    # Extract the translated text from the response
    data = response.json()
    translated_text = data[0][0][0]

    return translated_text

def update_chat_log():
    # Read the latest chat messages from the log file
    with open(chat_log_file, 'r', encoding='utf-8') as f:
        chat_log = f.read()

    # Extract the latest chat message
    latest_message = chat_log.splitlines()[-1]

    # Translate the latest message
    translated_message = translate_message(latest_message)

    # Display the translated message in the GUI window
    window["-OUTPUT-"].update(translated_message + '\n', append=True)

def monitor_chat_log():
    last_mtime = os.stat(chat_log_file).st_mtime
    while True:
        time.sleep(1)
        mtime = os.stat(chat_log_file).st_mtime
        if mtime != last_mtime:
            last_mtime = mtime
            update_chat_log()

# Start monitoring the chat log file in a separate thread
import threading
monitor_thread = threading.Thread(target=monitor_chat_log, daemon=True)
monitor_thread.start()

# Start updating the chat log
update_chat_log()

# Start the GUI event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

window.close()