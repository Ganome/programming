"""This will define the car class"""

class car:
    def __init__(self):
        self.__wheels = 4
        self.__windows = 6
        self.__doors = 4


class computer:
    def __init__(self):
        self.__CPU = 0
        self.__RAM = 0
        self.__STORAGE = 0
        self.__FIREWALL = 0
        self.__AV = 0
        self.__OS = 0
        self.__NETWORK = 0

    def setCPU(self, speed):
        self.__CPU = speed
    def setRAM(self, ram):
        self.__RAM = ram
    def setSTORAGE(self, storage):
        self.__STORAGE = storage
    def setOS(self, os):
        self.__OS = os
    def setNETWORK(self, network):
        self.__NETWORK = network

    def newComputer(self, cpu, ram, storage, os, network):
        self.__CPU = cpu
        self.__RAM = ram
        self.__STORAGE = storage
        self.__OS = os
        self.__NETWORK = network


myPC = computer()
myPC.setCPU(500)
myPC.setRAM(32)

print(myPC._computer__CPU, myPC._computer__RAM)
