from openai import OpenAI, RateLimitError
import openai
import speech_recognition as sr
import win32com.client as wc
from apiKey import Api_key


def say(text):
    speaker = wc.Dispatch("SAPI.SpVoice")

    speaker.Voice = speaker.GetVoices("gender=female").Item(0)

    speaker.speak(text)


def listen():
    print('listening...')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        audio = r.listen(source)
        try:
            print('Recognition...')
            query = r.recognize_google(audio, language="en-PK")
            print(f'User said: {query}')
            return query
        except Exception as e:
            print(f"An error occurred: {e}")
            return 'Some Error Occurred. Sorry! from Anna Balla'


if __name__ == '__main__':
    print("Hy! I am Anna_Balla A.I.")
    say("Hy! I am Anna Balla A I.")

    openai.api_key = "Api_key"

    client = OpenAI(api_key=openai.api_key)

    while True:
        query = listen()
        user_input = query  # Replace with your own input function
        if user_input == "quit":
            print("Goodbye!")
            break

        try:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a personalized chatbot, known as Anna Balla, skilled in explaining complex programming concepts with creative flair."},
                    {"role": "user", "content": user_input}
                ]
            )
            chatbot_response = completion.choices[0].message.content
            print(chatbot_response)
            say(chatbot_response)

        except RateLimitError as e:
            print(f"Rate limit exceeded. Details: {e}")
