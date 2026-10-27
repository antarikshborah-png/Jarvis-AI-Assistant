"""
Jarvis AI Voice Assistant
A beginner-friendly Python voice assistant with basic commands and optional OpenAI chat.
"""

import os
import random
import webbrowser
from datetime import datetime

import pyttsx3
import speech_recognition as sr
from dotenv import load_dotenv

load_dotenv()

ASSISTANT_NAME = "Jarvis"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()

speaker = pyttsx3.init()
speaker.setProperty("rate", 175)


def speak(message: str) -> None:
    """Speak a message and print it in the terminal."""
    print(f"{ASSISTANT_NAME}: {message}")
    speaker.say(message)
    speaker.runAndWait()


def listen() -> str:
    """Listen through the default microphone and return recognized text."""
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("\nListening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)

        print("Recognizing...")
        return recognizer.recognize_google(audio).lower().strip()

    except sr.WaitTimeoutError:
        return ""
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please try again.")
        return ""
    except sr.RequestError:
        speak("Speech recognition is unavailable. Check your internet connection.")
        return ""
    except OSError:
        speak("I couldn't access your microphone. Check your microphone settings.")
        return ""


def ask_openai(prompt: str) -> str:
    """Use OpenAI when an API key is configured; otherwise return setup guidance."""
    if not OPENAI_API_KEY:
        return (
            "The AI chat feature is not configured yet. Add your OpenAI API key "
            "to a local .env file to enable it."
        )

    try:
        from openai import OpenAI

        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
            input=prompt,
        )
        answer = response.output_text.strip()
        return answer or "I couldn't generate a response just now."
    except Exception as exc:
        print(f"OpenAI error: {exc}")
        return "I couldn't connect to the AI service. Check your API key and connection."


def handle_command(command: str) -> bool:
    """Run a recognized command. Return False to stop the assistant."""
    if not command:
        return True

    if any(word in command for word in ("exit", "quit", "stop jarvis", "goodbye")):
        speak("Goodbye! Have a great day.")
        return False

    if "time" in command:
        speak(f"The time is {datetime.now().strftime('%I:%M %p')}.")
    elif "date" in command or "today" in command:
        speak(f"Today is {datetime.now().strftime('%A, %d %B %Y')}.")
    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
    elif "open github" in command:
        speak("Opening GitHub.")
        webbrowser.open("https://github.com")
    elif command.startswith("search for "):
        query = command.removeprefix("search for ").strip()
        if query:
            speak(f"Searching the web for {query}.")
            webbrowser.open("https://www.google.com/search?q=" + query.replace(" ", "+"))
        else:
            speak("Tell me what you want to search for.")
    elif "joke" in command:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "There are 10 kinds of people: those who understand binary and those who don't.",
            "Why did the computer get cold? It left its Windows open.",
        ]
        speak(random.choice(jokes))
    elif command.startswith("ask jarvis "):
        question = command.removeprefix("ask jarvis ").strip()
        speak(ask_openai(question))
    elif command in {"help", "what can you do"}:
        speak(
            "You can ask for the time or date, open Google, YouTube, or GitHub, "
            "say search for followed by a topic, ask for a joke, or say ask Jarvis "
            "followed by a question if the AI API is configured. Say stop Jarvis to exit."
        )
    else:
        speak("I don't know that command yet. Say help to hear the available commands.")

    return True


def main() -> None:
    speak("Hello! I am Jarvis, your Python voice assistant.")
    speak("Say help to hear what I can do.")

    running = True
    while running:
        command = listen()
        if command:
            print(f"You: {command}")
            running = handle_command(command)


if __name__ == "__main__":
    main()
