#!/usr/bin/python3
tenThings = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = tenThings.split(' ')
moreStuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    nextOne = moreStuff.pop() #pop pulls the last index first, unless otherwise specified inside the ()
    print(f"Adding {nextOne} to the list")
    stuff.append(nextOne)
    print(f"There are {len(stuff)} items now.")

print(f"There we go: {stuff}")

print("Let's do some things with stuff!")


print(stuff[1])
print(stuff[-1]) #should be end of list
print(stuff.pop())
print(' '.join(stuff))#This prints the entire list using and seperates entries with a space
print(" # ".join(stuff[3:5])) #this joins index 3 and index 5, with a "#" in between

print(f"Length of list: {len(stuff)}")