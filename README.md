# 🎙️ RASA AI — Python Desktop Voice Assistant

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Speech Recognition](https://img.shields.io/badge/Library-SpeechRecognition-yellow.svg)](https://pypi.org/project/SpeechRecognition/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Author](https://img.shields.io/badge/Author-Shivani%20PR-purple.svg)](https://github.com/Shivani8912)

A voice-controlled desktop AI personal assistant built with Python that listens to voice commands, responds with speech synthesis, executes web searches, opens frequently visited sites, reports weather updates, and answers conversational queries.

---

## 📌 Project Overview

**RASA AI** is an interactive virtual assistant designed to simplify desktop multitasking through hands-free voice commands. By combining real-time speech recognition with text-to-speech feedback, RASA listens through your microphone, interprets user intent, and provides instant audio and browser responses.

---

## 🌟 Key Features

- **🗣️ Real-Time Speech Recognition:** Utilizes Google's speech recognition engine with dynamic ambient noise adjustment to accurately capture voice queries.
- **🔊 Voice Synthesis (TTS):** Speaks responses aloud, greeting the user and confirming commands with clear speech.
- **🌐 Hands-Free Web Navigation:** Automatically opens popular platforms directly in your default browser on command:
  - *"Open YouTube"* → launches YouTube
  - *"Open Wikipedia"* → launches Wikipedia
  - *"Open Google"* → launches Google
- **🔍 Voice Google Search:** Dictate any search query verbally (e.g., *"Search for quantum computing"*), and RASA will query Google and display the results.
- **🌤️ City Weather Reports:** Inquires about current weather conditions for major cities (e.g., Bengaluru, Delhi, Mumbai, Chennai, Hyderabad) with natural spoken summaries.
- **⏰ Real-Time Clock:** Instantly announces the current time in 12-hour format upon request (*"What time is it?"*).
- **💬 Conversational Knowledge Base:** Responds to identity and casual chat queries (*"Who created you?"*, *"What can you do?"*, *"How are you?"*).
- **🛑 Voice Exit Command:** Gracefully terminates the assistant when you say *"bye"*, *"exit"*, *"stop"*, or *"quit"*.

---

## 🏗️ Architecture & Interaction Flow

```
[ Microphone Input ]
         │
         ▼
[ SpeechRecognition Engine ] ──► (Google Speech API)
         │
         ▼
[ Intent Parser & Query Handler ]
    ├── "open <site>"     ──► Browser Automation (webbrowser)
    ├── "search / google" ──► Google Web Search Query
    ├── "weather"         ──► City Weather Lookup
    ├── "time"            ──► System Clock (datetime)
    ├── Custom Query      ──► Conversational Dictionary
    └── "exit / quit"     ──► Graceful Shutdown
         │
         ▼
[ Voice Synthesis Engine ] ──► Spoken Response ("say") + Console Log
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Working microphone and audio output
- Internet connection (for Google Speech Recognition)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Shivani8912/RASA_AI.py.git
   cd RASA_AI.py
   ```

2. **Install dependencies:**
   ```bash
   pip install SpeechRecognition pyaudio
   ```
   > **Note for macOS users:** If installing `pyaudio` fails, install PortAudio via Homebrew first:
   > ```bash
   > brew install portaudio
   > pip install pyaudio
   > ```

3. **Run the assistant:**
   ```bash
   python RASA_AI.py
   ```
   *(On macOS / Linux: `python3 RASA_AI.py`)*

---

## 🗣️ Sample Voice Commands

| Category | What You Say | Assistant Action |
| :--- | :--- | :--- |
| **Greeting** | *"How are you?"* | Replies: *"I'm doing great! Thanks for asking."* |
| **Identity** | *"Who created you?"* | Replies: *"I was created by Shivani using Python!"* |
| **Web Navigation** | *"Open YouTube"* | Opens YouTube in your default browser |
| **Search** | *"Search on Google"* | Prompts for your search topic and opens search results |
| **Time** | *"What is the time?"* | Announces current local time |
| **Weather** | *"Check weather"* | Prompts for city and reports temperatures |
| **Shutdown** | *"Goodbye RASA"* / *"Exit"* | Bids farewell and shuts down |

---

## 🛠️ Tech Stack

- **Language:** Python
- **Speech Recognition:** `SpeechRecognition`, Google Speech API
- **Audio Processing:** `PyAudio`
- **Text-to-Speech:** macOS `say` utility / TTS engine
- **Web Automation:** Python `webbrowser` library

---

## 👤 Author

**Shivani PR**
- GitHub: [@Shivani8912](https://github.com/Shivani8912)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
