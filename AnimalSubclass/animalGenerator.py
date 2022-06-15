import subclass
from subclass import *

def main():
    animal_list = ""
    print("Welcome to the animal generator!")
    print("This program creates Animal objects.\n")
    while True:
        choice = input("would you like to create a mammal (1) or a bird (2)? ")
        if choice == '1':
            typee = input("what type of mammal would you like to create? ")
            name = input("what is the mammals name? ")
            haircolor = input("what color is the mammal's hair? ")
            useranimal = Mammal(name,typee, haircolor)
            animal_list += get_name(useranimal) + " the " + get_type(useranimal) + " is " + get_mood(useranimal) + "\n"
        elif choice == '2': 
            typee = input("what type of bird would you like to create? ")
            name = input("what is the birds name? ")
            canfly = input("can the bird fly? ")
            useranimal = Bird(name,typee, canfly)
            animal_list += get_name(useranimal) + " the " + get_type(useranimal) + " is " + get_mood(useranimal) + "exclusive attributes" + "\n"
        else:
            print("please enter a valid number")
            continue

        choice = input('\nWould you like to add more animals (y/n)? ')
        if choice == 'y':
            continue 
        else:
            print("\nAnimal List:\n",animal_list)
            break


main()