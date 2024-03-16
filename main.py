# this packages first you need to install in your pc or code editor

# here I'm using python 3.11 and using pycharm as code editor

"""
pip install speechrecognition
pip install wikipedia
pip install openai
pip install pywin32
python -m pip install pyaudio
pip install setuptools
pip install distutils-pytest
"""
# Import necessary packages


import openai  # OpenAI package
from openai import OpenAI, RateLimitError  # OpenAI package
import speech_recognition as sr  # Speech recognition package
import win32com.client as wc  # Windows-specific package for text-to-speech
import webbrowser as wb  # Web browsing package
import datetime as dt  # Date and time package
import asyncio  # Asynchronous I/O package for concurrent execution
from apiKey import Api_key


def say(query):  # Define a function to speak out text
    speaker = wc.Dispatch("SAPI.SpVoice")  # Initialize the SAPI.SpVoice speech engine
    speaker.Voice = speaker.GetVoices("gender=female").Item(0)  # Set the voice to female
    speaker.speak(query)  # Speak the provided query


def listen():  # Define a function to listen for user input through microphone
    print('listening...\n')
    try:
        r = sr.Recognizer()  # Initialize the recognizer
        with sr.Microphone() as source:  # Use the microphone as the audio source
            r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            audio = r.listen(source, timeout=5)  # Listen for audio with a timeout
        print('Recognition...\n')
        query = r.recognize_google(audio, language="en-PK")  # Recognize speech using Google Speech Recognition API
        print(f'Miss Qirat said: {query}')
        return query
    except sr.WaitTimeoutError:  # Handle timeout error
        print("Timeout occurred while listening.")
        return None
    except sr.UnknownValueError:  # Handle unknown value error
        print("Unable to recognize speech.")
        return None
    except Exception as e:  # Handle other exceptions
        print(f"An error occurred: {e}")
        return None


async def chatbot(query):  # Define an asynchronous function to interact with OpenAI chatbot

    openai.api_key = "Api_key"  # Set the OpenAI API key
    client = OpenAI(api_key=openai.api_key)  # Initialize OpenAI client

    try:
        user_input = query  # Set the user input
        loop = asyncio.get_event_loop()  # Get the event loop

        # Generate chatbot response using GPT-3.5 model
        completion = await loop.run_in_executor(None, lambda: client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a personalized chatbot, known as Anna Balla, skilled in explaining complex programming concepts with creative flair."},
                {"role": "user", "content": user_input}
            ]
        ))
        chatbot_response = completion.choices[0].message.content  # Get the chatbot response
        print("\n Anna Balla:", chatbot_response)
        say(chatbot_response)  # Speak the chatbot response

    except RateLimitError as e:  # Handle rate limit exceeded error
        print(f"\n Rate limit exceeded. Details: {e}")

# Main function
if __name__ == '__main__':
    print("\n Hy! I am Anna_Balla A.I. \n ")
    say("Hy! I am Anna Balla A I.")

    while True:
        query = listen()  # Listen for user input
        apps = [
            ['visual studio code', rf"C:\Users\LUCKY COMPUTER\OneDrive\Desktop\Visual Studio Code.lnk"],
            ["pycharm", rf"C:\Users\LUCKY COMPUTER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\JetBrains Toolbox\PyCharm Community.lnk"],
            ['opera', rf"C:\Users\LUCKY COMPUTER\OneDrive\Desktop\Opera Browser.lnk"]
        ]
        websites = [
            ["youtube", "https://www.youtube.com"],
            ["google", "https://www.google.com"],
            ["canva", "https://www.canva.com"]
        ]
        try:
            if any(f'open {app[0]}'.lower() in query.lower() for app in apps):  # Check if query is to open an app
                matching_app = next(app for app in apps if f'open {app[0]}'.lower() in query.lower())
                say(f'Opening {matching_app[0]} mam...')
                wb.open(matching_app[1])  # Open the corresponding application

            elif any(f'open {website[0]}'.lower() in query.lower() for website in websites):  # Check if query is to open a website
                matching_website = next(website for website in websites if f'open {website[0]}'.lower() in query.lower())
                say(f'Opening {matching_website[0]} mam...')
                wb.open(matching_website[1])  # Open the corresponding website

            elif "time" in query:  # Check if query is to get the current time
                hour = dt.datetime.now().strftime("%H")
                min = dt.datetime.now().strftime("%M")
                sec = dt.datetime.now().strftime("%S")
                say(f"Mam time is {hour} hour {min} minutes and {sec} seconds.")
                print(f"Mam time is {hour} hour {min} minutes and {sec} seconds.")

            elif "ok stop" in query:  # Check if query is to stop the program
                print('\n Stopping...')
                say("Goodbye! Have a great day.")
                break

            else:  # If none of the above conditions are met, interact with chatbot
                loop = asyncio.get_event_loop()
                loop.run_until_complete(chatbot(query))

        except Exception as e:  # Handle other exceptions
            print(f"\n An error occurred: {e}")
            say("Some error occurred. Sorry!")

    say(query)  # Speak the final query
