import speech_recognition as sr

def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"YOu Said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
        except sr.RequestError as e:
            print(f"Could not request results; check your network connection; {e}")

recognize_speech()