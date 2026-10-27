# Jarvis AI Voice Assistant 🤖

A beginner-friendly Python voice assistant that listens to voice commands and responds out loud. This project is designed as a learning project and a starting point for a personal assistant.

## Features

- Voice input through your microphone
- Spoken responses using text-to-speech
- Tells the current time and date
- Opens Google, YouTube, and GitHub
- Searches Google for a spoken topic
- Tells a programming joke
- Optional AI responses through the OpenAI API
- Keeps API keys in a local `.env` file instead of source code

## Tech Stack

- Python
- SpeechRecognition
- pyttsx3
- python-dotenv
- OpenAI Python SDK (optional AI chat)

## Requirements

- Python 3.10 or newer recommended
- A microphone
- Internet access for Google speech recognition and web searches
- An OpenAI API key only if you want to use the optional `ask jarvis ...` feature

## Setup

### 1. Download or clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Jarvis-AI-Assistant.git
cd Jarvis-AI-Assistant
```

### 2. Create and activate a virtual environment (recommended)

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

**Microphone dependency note:** `PyAudio` installation can vary by operating system and Python version. If installation fails, consult the PyAudio installation instructions for your platform.

### 4. Configure optional AI chat

If you want AI-powered answers:

1. Copy `.env.example` to a new file named `.env`.
2. Add your own API key after `OPENAI_API_KEY=`.
3. Keep `.env` private. It is excluded by `.gitignore`.

The assistant's regular voice commands work without an OpenAI API key.

### 5. Run Jarvis

```bash
python jarvis.py
```

Say **“help”** to hear supported commands.

## Voice Commands

| Say | What Jarvis does |
|---|---|
| `help` | Lists available commands |
| `what time is it` | Announces the current time |
| `what is today's date` | Announces the date |
| `open Google` | Opens Google |
| `open YouTube` | Opens YouTube |
| `open GitHub` | Opens GitHub |
| `search for machine learning` | Searches Google |
| `tell me a joke` | Tells a programming joke |
| `ask Jarvis explain neural networks` | Uses the optional OpenAI feature |
| `stop Jarvis` | Exits the assistant |

## Privacy and Security

- The default speech recognition uses Google's online speech recognition service, so recognized audio is processed by that service.
- The optional AI feature sends your prompt to the OpenAI API.
- Never commit API keys, `.env` files, passwords, or other secrets to GitHub.
- Review commands before adding features that control files, devices, or external services.

## Project Structure

```text
Jarvis-AI-Assistant/
├── jarvis.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Future Improvements

- Add a graphical user interface
- Add custom wake-word detection
- Add more useful commands
- Add configurable voice and language options
- Add unit tests

## Author

Antariksh Borah

---

This is a learning project. Update the README and features as you customize the assistant.
