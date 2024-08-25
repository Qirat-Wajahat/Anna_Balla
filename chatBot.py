import openai                              # OpenAI package
import asyncio                             # Asynchronous I/O package for concurrent execution
from openai import OpenAI, RateLimitError  # OpenAI package
from say import say
from config import Api_key


# Asynchronous function to interact with OpenAI chatbot
async def chatbot(query):
    openai.config = "Api_key"  # Set the OpenAI API key
    client = OpenAI(config=openai.config)  # Initialize OpenAI client

    try:
        user_input = query
        loop = asyncio.get_event_loop()  # Get the event loop

        # Generate chatbot response using GPT-3.5 model
        completion = await loop.run_in_executor(
            None, lambda: client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a personalized chatbot, known as Anna Balla, skilled in explaining complex programming concepts with creative flair."
                    },
                    {"role": "user", "content": user_input}
                ]
            )
        )

        chatbot_response = completion.choices[0].message.content  # Get the chatbot response
        print("\n Anna Balla:", chatbot_response)
        say(chatbot_response)  # Speak the chatbot response

    except RateLimitError as e:
        print(f"\n Rate limit exceeded. Details: {e}")

