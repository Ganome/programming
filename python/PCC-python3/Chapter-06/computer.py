class Computer:
    def __init__(self):
        self.__CPU = 0
        self.__CORES = 0
        self.__POWER = self.__CORES * self.__CPU
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

    def newComputer(self, cpu, cores, ram, storage, os, network):
        self.__CPU = cpu
        self.__CORES = cores
        self.__POWER = cpu * cores
        self.__RAM = ram
        self.__STORAGE = storage
        self.__OS = os
        self.__NETWORK = network

    def printSpecs(self):
        print("Current computer Specs are as follows:\nCPU: ", self.__CPU, "Mhz @", self.__CORES, "Total Power: ", self.__POWER, "\nRAM: ", self.__RAM, "\nStorage: ", self.__STORAGE, "Terabytes\nOperating System: ", self.__OS, "\nNetwork Connection: ", self.__NETWORK)


