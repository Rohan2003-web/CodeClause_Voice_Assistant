import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function for vocalizing given text
def vocalize(text):
    engine.say(text)
    engine.runAndWait()

# Function for receiving speech input from the user
def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User: {query}")
    except Exception as e:
        print("Please repeat that...")
        return "None"
    return query

# Main execution
if __name__ == "__main__":
    vocalize("Greetings! I am your AI assistant. How may I assist you today?")

    while True:
        user_query = listen_for_command().lower()

        if "hello" in user_query:
            vocalize("Hello! How can I be of service?")
        elif "how are you" in user_query:
            vocalize("I'm merely a machine, but I'm here to aid you!")
        elif "open youtube" in user_query:
            vocalize("Launching YouTube...")
            webbrowser.open("https://www.youtube.com/")
        elif "open gmail" in user_query:
            vocalize("Accessing Gmail...")
            webbrowser.open("https://mail.google.com/")
        elif "open chrome" in user_query:
            vocalize("Starting Google Chrome...")
            webbrowser.open("https://www.google.com/chrome/")
        elif "bye" in user_query:
            vocalize("Farewell! Have a splendid day.")
            break
        else:
            vocalize("I apologize, I'm not familiar with that command.")
