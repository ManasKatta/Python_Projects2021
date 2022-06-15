import random
from random import randint
class Animal:
    def __init__(self,__name,__animal_type):
        mood_number= randint(1,3)
        self.__name = __name 
        self.__mood = mood_number
        self.__animal_type = __animal_type
        if (mood_number==1):
            self.__mood = "happy"
        elif (mood_number == 2):
            self.__mood = "hungry"
        elif (mood_number == 3):
            self.__mood = "sleepy"
        


def get_mood(animal):
    return animal._Animal__mood

def get_name(animal):
    return animal._Animal__name

def get_type(animal):
    return animal._Animal__animal_type

