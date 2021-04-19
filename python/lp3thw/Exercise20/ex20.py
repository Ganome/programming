from sys import argv

script, inputFile = argv

def printAll(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def printALine(lineCount, f):
    #print(lineCount, f.readline())  #THIS METHOD INCLUDES THE LINE NUMBER!!!
    print(f.readline())

currentFile = open(inputFile)

print("First let's print the whole file: \n")
printAll(currentFile)

print("Now let's rewind. Kind of like a tape.")

rewind(currentFile)

print("Let's print three lines:")

currentLine = 1
printALine(currentLine, currentFile)

currentLine += 1
printALine(currentLine, currentFile)

currentLine = currentLine + 1 #THIS is identical to the line above!
printALine(currentLine, currentFile)