from clock import Clock

localTime = Clock()

localTime.printTime()
localTime.setTime(23, 59, 59)
localTime.printTime()

#print (localTime._Clock__second) #THIS IS how you access private or mangled variable names

#localTime.setSeconds("37")
#localTime.setHours(4)
#localTime.setMinutes(20)
localTime.tick()
localTime.printTime()

#print ("The class for is ",localTime,  localTime.__class__) #This line prints out the memory address

control = 1
loop = 150
while control < loop:
    localTime.printTime()
    localTime.tick()
    control = control + 1
