x = object()
y = object()

xList = []
yList = []
#bigList = xList + yList

#Create the X list
xList.append(1)
xList.append(2)
xList.append(3)
xList.append(4)
xList.append(5)
xList.append(6)
xList.append(7)
xList.append(8)
xList.append(9)
xList.append(10)
#Create the Ylist
yList.append(10)
yList.append(9)
yList.append(8)
yList.append(7)
yList.append(6)
yList.append(5)
yList.append(4)
yList.append(3)
yList.append(2)
yList.append(1)

bigList = (xList + yList) * 10
print (xList, "\n", yList)
print ("The Big list follows : ", bigList)

print ("\n", "The X list contains : ", len(xList))
print ("The Y list contains : ", len(yList))
print ("The bigList is : ", len(bigList))

