#!/bin/python3

from sys import argv

script, userName, likeLevel = argv
prompt = "Well? - "

print(f"Hi {userName}, I'm the {script} script")
print("I'd like to ask you a few questions: ")
print(f"Do you like me {userName}")
likes = input(prompt)
print(f"Where you live {userName}?")
lives = input(prompt)
print(f"What kind of Computer do you have?")
computer = input(prompt)
print(f"""
Alright, so you said {likes} about liking me.
Your likeness level was {likeLevel}.  What did i do?
You reside in {lives}. Where is that exactly?
And you have a {computer} computer.
""")