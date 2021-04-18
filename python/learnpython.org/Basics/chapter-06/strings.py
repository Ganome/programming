aString = "Hello World!"

print ("Use aString.index(\"LETTER\") to return the first time that letter appears")
        
print ("The first time o appears is at index : ", aString.index("o")) # returns what place in the string matches the specified character "o" in this case INDEX STARTS AT ZERO!!

print ("L appears : ", aString.count("l"), "Times") # returns how many times the specified character appears in the string

print ("\n\nTo return specific portions of a string use aString[start:stop]")
print (aString[3:7]) # Will return from the index position 3-7 in the string.

print (aString[0:5:2]) #This is stepping, meaning you want to only see every 2nd character.

#
print (aString[:-1:])

print ("\n\nTo print a string backwords use this syntax print (aString[::-1])")
print (aString[::-1])

#to retrieve the last x amount of characters

print (aString[-1:5]) #This will fetch the last 5 characters

print ("\n\nTo retrieve a specified length, starting from the beginning of the file, use the syntax aString[:LENGTH]")
print (aString[:5])

print ("\n\n to retrieve a specified length, starting from the end of the file, use syntax aString[-5:]")
print (aString[-5:])

print ("\n\nTo retrieve the entire string, after a specified character, use syntax aString[4:] ")
print (aString[4:])


print ("There are also UPPER and LOWER functions for strings!")
print (aString.upper())
print (aString.lower())


print ("\n\nWe can determine if a string starts or ends with a certain sequence by using: aString.startswith(\"\") and aString.endswith(\"\")")
print (aString.startswith("Hello"))

print ("\n\n You can split strings into multiple strings by using aString.split(\" \")")
newString = aString.split(" ")
print (newString)
print ("It creates a new table, with each string as its entry or index")
