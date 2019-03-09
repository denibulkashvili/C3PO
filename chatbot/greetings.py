"""
Defines greetings inputs and responses
"""
import random

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey", "good morning")
GREETING_RESPONSES = ["Hello, Sir", "Greetings, Human.",]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
