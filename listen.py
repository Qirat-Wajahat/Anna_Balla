# Speech recognition package
import speech_recognition as sr

# Function to listen for user input through microphone
def listen():
    print('Listening...\n')
    try:
        r = sr.Recognizer()  # Initialize the recognizer
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            audio = r.listen(source, timeout=5)  # Listen for audio with a timeout
        print('Recognition...\n')
        query = r.recognize_google(audio, language="en-PK")  # Recognize speech using Google Speech Recognition API
        print(f'Miss Qirat said: {query}')
        return query
    except sr.WaitTimeoutError:
        print("Timeout occurred while listening.")
        return None
    except sr.UnknownValueError:
        print("Unable to recognize speech.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None