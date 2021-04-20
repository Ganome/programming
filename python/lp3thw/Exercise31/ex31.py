print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input(" Decision > ")

if door == "1":
    print("There's a giant bear here eating a chese cake.")
    print("What do you do?")
    print("1.\tTake the cake.\n2.\tScream at the bear")

    bear = input(" Decision > ")

    if bear == "1":
        print("The bear eats your face off. Good Job!")
    elif bear == "2":
        print("The bear eats your legs off! Good luck getting away!")
    else:
        print(f"Well, doing {bear} is probably better")
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina")
    print("1.\tBlueberries\n2.\tYellow jacket clothespins.\n3.\tUnderstanding revolvers yelling melodies.")

    insanity = input(" Decision > ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.\nGOOD JOB!!!")
    else:
        print("You stumble around and fall on a knife and die.\nWONDERFUL!!")
