#!/usr/bin/python3
from sys import exit

def goldRoom():
    print("This room is full of gold. How much do you take?")

    choice = input("Greedy? > ")
    if "0" in choice or "1" in choice:
        howMuch = int(choice)
    else:
        dead("Man, learn to type a number.")

    if howMuch < 50:
        print("Nice, you're not that greedy.\n\t\t***YOU WIN***")
        exit(0)
    else:
        dead("You greedy bastard!!")


def bearRoom():
    print("There is a bear in this room!")
    print("The bear has a bunch of honey.\nThe fat bear is in front of another door.")
    print("How are you going to move the bear?")
    print("'take honey' , 'taunt bear' , 'openP door'")
    bearMoved = False

    while True:
        choice = input(" > ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off!")
        elif choice == "taunt bear" and not bearMoved:
            print("The bear has moved from the door.\nYou can now go through!")
            bearMoved = True
        elif choice == "taunt bear" and bearMoved:
            goldRoom()
        elif choice == "open door" and bearMoved:
            goldRoom()
        elif choice == "open door" and not bearMoved:
            dead("You tried to push through the door and the bear ate you instead of the honey!")
        else:
            print("I got no idea what that means. Please try again")

def cthulhuRoom():
    print("Here you see the great evil cthulhu.\nHe, it, whatever stares at you and you go inside.")
    print("Do you flee for your life or eat your own head?")

    choice = input("Dine or Dash? > ")
    if "Dash" in choice or "dash" in choice:
        start()
    elif "Dine" in choice or "dine" in choice:
        dead("Well aren't you tasty?")
    else:
        cthulhuRoom()


def dead(why):
    print("\n", why, "\nGood Job, you are DEAD!!!\v\v")
    #Adding in an option to play again
    choice = input("Would you like to play again?\nYes or No\n>")
    if choice == "yes" or choice == "Yes":
        start()
    elif choice == "no" or choice == "No":
        exit(0)
    else:
        print("Not a a valid answer!!")

def start():
    print("You are in a dark room.\nThere is a door to your right and left")
    #print("Which door do you walk through??")
    #choice = input(" > ")
    choice = input("Which door do you walk through??\n>")

    if "Left" in choice or "left" in choice:
        bearRoom()
    elif "Right" in choice or "right" in choice:
        cthulhuRoom()
    else:
        dead("You stumbled around and wondered yourself to death.")

start()