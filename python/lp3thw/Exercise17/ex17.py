from sys import argv
from os.path import exists

script, fromFile, toFile = argv

print(f"Copying from {fromFile} into {toFile}")

inFile = open(fromFile)
inData = inFile.read()

print(f"The input file is {len(inData)} bytes long.")

print(f"Does the output file exist? {exists(toFile)}")
print("Ready? hit RETURN to continue - ")

input(" ------ ")

outFile = open(toFile, "w") #use mode to so we make sure its a clean copy.  Erases the file on opening
outFile.write(inData)

outFile.close()
inFile.close()