import speech_recognition as sr
import os
import webbrowser
import datetime
import time
import sys
import traceback

# ---------- SPEAK FUNCTION ----------
def say(text):
    try:
        os.system(f"say \"{text}\"")
    except:
        print(text)

# ---------- LISTEN FUNCTION ----------
def takeCommand(timeout=5, phrase_time_limit=6):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print("You said:", query)
            return query.lower().strip()
        except:
            return ""

# ---------- CUSTOM ANSWERS ----------
custom_answers = {
    "who created you": "I was created by Shivani using Python!",
    "who made you": "I was made by Shivani!",
    "what can you do": "I can open websites, tell the weather, time, and answer your questions!",
    "how are you": "I’m doing great! Thanks for asking.",
    "your name": "I’m RASA, your virtual assistant.",
    "who are you": "I’m your AI assistant RASA, made by Shivani!"
}

# ---------- WEATHER WITHOUT API ----------
def get_weather(city):
    weather_data = {
        "bengaluru": "The weather in Bengaluru is pleasant with 28 degrees.",
        "bangalore": "The weather in Bengaluru is pleasant with 28 degrees.",
        "delhi": "Delhi is warm today with 32 degrees.",
        "mumbai": "Mumbai is humid with 30 degrees.",
        "chennai": "Chennai is hot with 34 degrees.",
        "hyderabad": "Hyderabad has mild weather with 29 degrees."
    }

    city = city.lower()

    if city in weather_data:
        return weather_data[city]
    else:
        return f"Sorry, I don't have weather information for {city}."

# ---------- MAIN PROGRAM ----------
def main():
    print("Starting RASA assistant...")
    say("Hello! I am RASA, your virtual assistant.")

    while True:
        query = takeCommand()

        if not query:
            continue

        executed = False

        # EXIT
        if any(word in query for word in ["exit", "stop", "bye", "quit"]):
            say("Goodbye Shivani! Have a nice day.")
            break

        # OPEN WEBSITES
        sites = [
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.org"],
            ["google", "https://www.google.com"]
        ]

        for site in sites:
            if f"open {site[0]}" in query:
                say(f"Opening {site[0]}, Madam.")
                webbrowser.open(site[1])
                executed = True
                break

        # TIME
        if "time" in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            say(f"Madam, the time is {current_time}.")
            executed = True

        # CUSTOM ANSWERS
        elif any(key in query for key in custom_answers):
            for key in custom_answers:
                if key in query:
                    say(custom_answers[key])
                    executed = True
                    break

        # WEATHER
        elif "weather" in query:
            say("Sure! Please tell me the city name.")
            city = takeCommand()

            if city:
                result = get_weather(city)
                print(result)
                say(result)
            else:
                say("Sorry, I couldn't hear the city name.")
            executed = True

        # GOOGLE SEARCH FEATURE (VOICE)
        elif "search" in query or "google" in query:
            say("What do you want to search on Google?")
            search_query = takeCommand()

            if search_query:
                say(f"Searching for {search_query}")
                url = f"https://www.google.com/search?q={search_query.replace(' ', '+')}"
                webbrowser.open(url)
            else:
                say("I didn’t hear the search topic.")
            executed = True

        # FALLBACK
        if not executed:
            say("Sorry, I didn't understand that. Please try again.")

# ---------- RUN ----------
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exited by user.")
        sys.exit(0)
    except Exception as e:
        print("Fatal error:", e)
        traceback.print_exc()
        sys.exit(1)