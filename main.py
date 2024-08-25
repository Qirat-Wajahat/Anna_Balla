# Import necessary packages

import webbrowser as wb                    # Web browsing package
import datetime as dt                      # Date and time package
import asyncio                             # Asynchronous I/O package for concurrent execution
from say import say
from listen import listen
from chatBot import chatbot

# Main function
if __name__ == '__main__':
    print("\n Hi! I am Anna Balla A.I. \n")
    say("Hi! I am Anna Balla A I.")

    while True:
        query = listen()  # Listen for user input

        # List of applications to open
        apps = [
            ['visual studio code', rf"C:\Users\LUCKY COMPUTER\OneDrive\Desktop\Visual Studio Code.lnk"],
            ["pycharm", rf"C:\Users\LUCKY COMPUTER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\JetBrains Toolbox\PyCharm Community.lnk"],
            ['opera', rf"C:\Users\LUCKY COMPUTER\OneDrive\Desktop\Opera Browser.lnk"]
        ]

        # List of websites to open
        websites = [
            ["youtube", "https://www.youtube.com"],
            ["google", "https://www.google.com"],
            ["canva", "https://www.canva.com"]
        ]

        try:
            # Check if the query is to open an app
            if any(f'open {app[0]}'.lower() in query.lower() for app in apps):
                matching_app = next(app for app in apps if f'open {app[0]}'.lower() in query.lower())
                say(f'Opening {matching_app[0]}...')
                wb.open(matching_app[1])  # Open the corresponding application

            # Check if the query is to open a website
            elif any(f'open {website[0]}'.lower() in query.lower() for website in websites):
                matching_website = next(website for website in websites if f'open {website[0]}'.lower() in query.lower())
                say(f'Opening {matching_website[0]}...')
                wb.open(matching_website[1])  # Open the corresponding website

            # Check if the query is to get the current time
            elif "time" in query:
                hour = dt.datetime.now().strftime("%H")
                min = dt.datetime.now().strftime("%M")
                sec = dt.datetime.now().strftime("%S")
                say(f"The current time is {hour} hours, {min} minutes and {sec} seconds.")
                print(f"The current time is {hour} hours, {min} minutes and {sec} seconds.")

            # Check if the query is to stop the program
            elif "ok stop" in query:
                print('\n Stopping...')
                say("Goodbye! Have a great day.")
                break

            # If none of the above conditions are met, interact with chatbot
            else:
                loop = asyncio.get_event_loop()
                loop.run_until_complete(chatbot(query))

        except Exception as e:
            print(f"\n An error occurred: {e}")
            say("An error occurred. Sorry!")
