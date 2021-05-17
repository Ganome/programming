from computer import Computer

myPC = Computer()

#myPC.setCPU(500)
#myPC.setRAM(32)
#print(myPC._Computer__CPU, myPC._Computer__RAM)

myPC.newComputer(2750, 6, 128, 8, "linux", "gigabit")
myPC.printSpecs()