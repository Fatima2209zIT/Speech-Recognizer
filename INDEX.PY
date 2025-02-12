import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to user input and return text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You: {text}")
            return text.lower()
        except sr.UnknownValueError:
            return "Sorry, I didn't understand that."
        except sr.RequestError:
            return "Request error, please check your internet."

def open_app(command):
    """Open apps based on user command"""
    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif "open gmail" in command:
        webbrowser.open("https://www.gmail.com")
        speak("Opening Gmail")
    elif "open instagram" in command:
        webbrowser.open("https://www.instagram.com")
        speak("Opening Instagram")
    elif "open wikipedia" in command:
        webbrowser.open("https://www.wikipedia.org")
        speak("Opening Wikipedia")
    else:
        speak("Sorry, I can't open that app yet.")

def search_wikipedia(query):
    """Search Wikipedia and return a summary"""
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError:
        return "There are multiple results. Please be more specific."
    except wikipedia.exceptions.PageError:
        return "No results found."

# Main chatbot loop
def chatbot():
    speak("Hello! How can I assist you?")
    while True:
        user_command = listen()

        if "exit" in user_command or "thanks bye" in user_command:
            speak("Goodbye! Have a great day!")
            break
        elif "open" in user_command:
            open_app(user_command)
        else:
            answer = search_wikipedia(user_command)
            speak(answer)

if __name__ == "__main__":
    chatbot()
