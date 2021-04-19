def cheeseAndCrackers(cheeseCount, boxesOfCrackers):
    print(f"You have {cheeseCount} cheeses!")
    print(f"You have {boxesOfCrackers} boxes of crackers")
    print("Man thats enough for a party!")
    print("Get a blanket!\n")

print("We can just give the function numbers directly")
cheeseAndCrackers(20, 30)

print("OR, we can use variables from our script:")

amountOfCheeses = 10
amountOfCrackers = 50

cheeseAndCrackers(amountOfCheeses, amountOfCrackers)

print("We can even do the math inside:")
cheeseAndCrackers(6 * 5, 24 + 16)

print("And we can combine the two, variables and math:")
cheeseAndCrackers(amountOfCheeses + 32,amountOfCrackers + 5 * 4)