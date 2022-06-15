import animal
from animal import *



def main():
    animal_list = ""
    print("Welcome to the animal generator!")
    print("This program creates Animal objects.\n")
    while True:
        typee = input("What type of animal would you like to create? ")
        name = input("\nWhat is the animal’s name? ")
        useranimal = Animal(name,typee)
        animal_list += get_name(useranimal) + " the " + get_type(useranimal) + " is " + get_mood(useranimal) + "\n"

        choice = input('\nWould you like to add more animals (y/n)? ')
        if choice == 'y':
            continue 
        else:
            print("\nAnimal List:\n",animal_list)
            break


main()