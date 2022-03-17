from nltk.chat.util import Chat, reflections
import speech_recognition as sr
import pyttsx3
from usecase.reflections import Bot_Reflections
from usecase.pairs import Bot_Pairs

rcg = sr.Recognizer()


def chat():
    print("Hi! I am a Fiona, created by Santosh for your service")
    engine = pyttsx3.init()
    bot_response = "Hi! I am a Fiona, created by Santosh for your service"
    engine.say(bot_response)
    engine.runAndWait()
    user_input_choice = input("Enter your choice:\n1.Text\n2.Voice\n")
    chat = Chat(Bot_Pairs.bot_pairs, Bot_Reflections.bot_reflections)
    converse = 1

    if user_input_choice == "Text":
        while converse:
            user_data = input("> ")
            if user_data == "quit":
                converse = 0
            bot_response = str(chat.respond(user_data))
            if bot_response == "None":
                bot_response = "I did not understand your query, please be more specific."
            print(bot_response)
            engine.say(bot_response)
            engine.runAndWait()
    else:
        def SpeakText(command):
            engine = pyttsx3.init()
            engine.say(command)
            engine.runAndWait()

        while converse:
            try:
                with sr.Microphone() as source:

                    print("Speak....")
                    audio = rcg.record(source, 5)
                    print("Audio input captured")
                    user_input = rcg.recognize_google(audio)
                    user_input = user_input.lower()
                    print("human:", user_input)
                    SpeakText(user_input)
                    if user_input == "quit":
                        converse = 0
                    bot_response = str(chat.respond(user_input))
                    if bot_response == "None":
                        bot_response = "I did not understand your query, please be more specific."
                    print(bot_response)
                    engine.say(bot_response)
                    engine.runAndWait()

            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

            except Exception as e:
                print("error:", e)


if __name__ == "__main__":
    chat()
