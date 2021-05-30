"""This will define the car class"""

class car:
    def __init__(self):
        self.__wheels = 4
        self.__windows = 6
        self.__doors = 4
        self.__horsepower = 100
        self.__totaled = False
        self.__color = "black"
        self.__customized = False

    def showOffCar(self):
        print(f"My car still has {self.__wheels} wheels\n{self.__windows} windows,\n{self.__doors} doors are attached,\nTotaled out: {self.__totaled},\nWith {self.__horsepower} horsepower!")
