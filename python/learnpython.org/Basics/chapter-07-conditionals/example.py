#! /bin/python3

x = 2

print ("x = 2")
print ("x == 2", x == 2)
print ("x == 3", x == 3)
print ("x != 2", x != 2)


name = "John"
age = 35

if name == "John" and age == 35:
    print("This is an indented statement, becaues it's inside an if clause.")
if name == "John" and age > 33:
    print("This is printed from an second if statement!")
else:
    print("None of the conditions were true")

#Now we'll iterate through lists

listNames = ["John", "Rick", "Morty"]
#Remeber the name variable is already set to "John"
if name in listNames:
    print("Found the name 'John' inside the listNames variable!")

#Now well dive into Code Blocks!!

statement = False
anotherStatement = True

if statement is True:
    #this is a code block!
    print("If statement was true, this would print out.  But its set to False.")
    pass
elif anotherStatement is True:
    #another nested code block under the elif statement!
    print("\n\nWe have found the variable anotherStatement as True")
    pass
else:
    print("Nothing has evaluated")
    pass

#Now wel start to use the "is" operator

list1 = [1, 2, 3]
list2 = ["one", "two", "three"]
list3 = [1, 2, 3]

print ("\n\nlist1 : ", list1, "\nlist2 : ", list2, "\nlist3 : ", list3)
print ("list1 == list2 : ", list1 == list2)
print ("list1 is list2 : ", list1 is list2)
print ("list1 == list3 : ", list1 == list3)
print ("list 1 is list3 : ", list1 is list3)


#now time for the not operator

print ("\n\nnot False : ", not False)
print ("(not False) == False : ", (not False) == False)

