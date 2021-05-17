class Clock:
    def __init__(self):
        self.__hour = 0
        self.__minute = 0
        self.__second = 0

    def setTime(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def tick(self):
        self.__second = self.__second + 1
        if (self.__second == 60):
            self.__second = 0
            self.__minute = self.__minute + 1
            if (self.__minute == 60):
                self.__hour = self.__hour + 1
                self.__minute = 0
                if (self.__hour == 24):
                    self.__hour = 0

    def printTime(self):
        print("The time is - ", self.__hour, ":", self.__minute, ":", self.__second)

    def setSeconds(self, second):
        if int(second) >= 0:
            if int(second) <= 59:
                self.__second = second
        else:
            return
    def setMinutes(self, minute):
        if int(minute) >= 0:
            if int(minute) <= 59:
                self.__minute = minute
        else:
            return
    def setHours(self, hour):
        self.__hour = hour
    #NOW WE'LL DEFINE OUR GETTERS
    def getSeconds(self):
        return self.__second
    def getMinutes(self):
        return self.__minute
    def getHours(self):
        return self.__hour
