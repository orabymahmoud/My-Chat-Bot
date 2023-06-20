from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import sys
import os
sys.path.append(os.path.dirname(__file__))


CORPUS_FILE = "chat.txt"

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
cleaned_corpus = CORPUS_FILE

def Bot_Train():
    trainer.train(cleaned_corpus)

def Bot_Train_Specific(message , response):
    trainer.train([
    message,
    response,
])

def Bot_Chat(message):
    return chatbot.get_response(message)
