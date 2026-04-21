# 🤖 JARVIS — Phase 1: Basic Voice Assistant

A modular voice assistant built in Python for Windows.

---

## 📁 Project Structure

```
jarvis/
│
├── main.py                  ← Entry point, run this
├── requirements.txt
│
└── jarvis/
    ├── __init__.py
    ├── listener.py          ← Microphone → Text (Speech Recognition)
    ├── speaker.py           ← Text → Voice (pyttsx3)
    ├── commands.py          ← All command logic lives here
    └── utils.py             ← Helpers (greeting, etc.)
```

---

## ⚙️ Setup (Windows)

### Step 1 — Install Python 3.8+
Download from https://python.org — tick "Add to PATH" during install.

### Step 2 — Install PyAudio (Windows-specific, must do FIRST)
PyAudio needs a pre-built wheel on Windows. Run:

```bash
pip install pipwin
pipwin install pyaudio
```

If that fails, try downloading the wheel directly:
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
Then: `pip install PyAudio‑0.2.11‑cp311‑cp311‑win_amd64.whl`

### Step 3 — Install remaining dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Run Jarvis
```bash
python main.py
```

---

## 🗣️ Supported Commands (Phase 1)

| You say...                     | Jarvis does...              |
|--------------------------------|-----------------------------|
| "What time is it?"             | Tells the current time      |
| "What's today's date?"         | Tells today's date          |
| "Open Chrome"                  | Launches Google Chrome      |
| "Open Notepad"                 | Launches Notepad            |
| "Open VS Code"                 | Launches VS Code            |
| "Open Calculator"              | Opens Calculator            |
| "Open YouTube"                 | Opens YouTube in browser    |
| "Search for black holes"       | Googles "black holes"       |
| "Tell me a joke"               | Cracks a dev joke           |
| "Hello / Hi"                   | Greets you back             |
| "Who are you?"                 | Introduces itself           |
| "Exit / Goodbye / Shut down"   | Shuts Jarvis down           |

---

## ➕ Adding New Commands

Open `jarvis/commands.py` and add to `handle_command()`:

```python
elif "your keyword" in command:
    speak("Your response here")
```

That's it. No other file needs to change.

---

## 🔜 Phase 2 Preview
- Connect OpenAI API for smart responses
- Conversation memory
- Handle unknown commands intelligently
```
