# 🛡️ Advanced Keylogger with Active Window Tracking (Educational Purpose)

## ⚠️ Disclaimer

> **This project is strictly for educational purposes.**  
> Do **not** use this software to monitor devices without proper consent. Unauthorized usage can lead to legal consequences.  
> Always respect privacy and adhere to your local cybersecurity laws and ethical guidelines.

---

## 📝 Description

This Python-based **Advanced Keylogger** logs keystrokes along with the **active window title** where the input occurred. The script is built using the `pynput` and `pywin32` libraries and records keystrokes in real-time while also logging when the user switches applications.

This project can be useful for:
- Security researchers and ethical hackers learning about keylogging techniques
- Parental control applications (with consent)
- Personal usage (e.g., tracking your own activity)

---

## 🧰 Features

- ⌨️ Records **all keystrokes**
- 🪟 Tracks and logs **active window title changes**
- 🕒 Timestamps all logs for clear tracking
- 📄 Saves logs to a human-readable text file
- 🧱 Built with `pynput`, `win32gui`, and `logging` modules

---

## 🚀 Getting Started

### ✅ Requirements

- Python 3.x
- Install dependencies:

```bash
pip install pynput pywin32
```

### ▶️ Run the Script

```bash
python advanced_keylogger.py
```

Logs will be saved to:

```
advanced_key_log.txt
```

### 🧪 Sample Log Output

```
2025-04-29 15:24:10,212: 

[Window Changed] Visual Studio Code - 2025-04-29 15:24:10.212958

2025-04-29 15:24:11,113: h
2025-04-29 15:24:11,221: e
2025-04-29 15:24:11,321: l
2025-04-29 15:24:11,421: l
2025-04-29 15:24:11,521: o
2025-04-29 15:24:12,021: [Key.space]
2025-04-29 15:24:12,121: w
2025-04-29 15:24:12,221: o
2025-04-29 15:24:12,321: r
2025-04-29 15:24:12,421: l
2025-04-29 15:24:12,521: d
```

---

## 🧠 How It Works

- Uses `pynput.keyboard.Listener` to monitor and log all keystrokes.
- Uses `win32gui` to detect the current **foreground window title**.
- Logs a timestamp every time the active window changes or a key is pressed.

---

## 📁 File Structure

```
advanced_keylogger.py     # Main script
advanced_key_log.txt      # Log file (auto-generated)
```

---

## 🔒 Security & Ethical Usage

- This tool is for **authorized testing** and **personal educational use**.
- Never use this on a system you do not own or manage **without explicit permission**.
- Modify the script responsibly if you're integrating it into research or controlled environments.

---

## 📃 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 📌 Enhancements You Could Add

- Auto-emailing logs
- GUI interface using Tkinter or PyQt
- Keyword alert triggers
- Log file encryption
- Cross-platform support (Linux/macOS)

