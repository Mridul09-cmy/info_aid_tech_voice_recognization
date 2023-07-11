import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        text = r.recognize_google(audio)
        print("Speech recognized: " + text)
    except sr.UnknownValueError:
        print("Speech could not be recognized.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Call the function to recognize speech
recognize_speech()
