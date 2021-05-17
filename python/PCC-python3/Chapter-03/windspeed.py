#!/usr/bin/python3

#This programs calculates what level a hurricane is based on Wind Speed
def hurricaneSpeeds():
    try:
        windSpeed = int(input("Please enter the current MPH in wind speed: "))

        while windSpeed:
            if windSpeed <= 73 and windSpeed > 0:
                print ("This isn't even a hurricane you Nancy!!")
                break #Without this break line, it will SPAM text at you in the console!!!
            elif windSpeed > 73 and windSpeed <= 95:
                print ("You've got yourself a Category 1 hurricane.")
                break #Without this break line, it will SPAM text at you in the console!!!
            elif windSpeed >= 96 and windSpeed <= 110:
                print ("This is a category 2 hurricane")
                break #Without this break line, it will SPAM text at you in the console!!!
            elif windSpeed >= 111 and windSpeed <= 130:
                print ("Getting up there, Category 3!!!")
                break
            elif windSpeed >=131 and windSpeed <= 155:
                print("Hope your safe, this is a Category 4!")
                break
            elif windSpeed > 155:
                print("If your not safe somewhere, bend over and kiss your ass goodbye.  This is a Category FIVE!!")
                break
            else:
                print("Hurricanes can't have winds less than ZERO miles per hour!!!\n*** Try Again ***")
                hurricaneSpeeds()
                break

    except:
        print("Please enter a number: 75, 120, 200, etc...")
        hurricaneSpeeds()

hurricaneSpeeds()