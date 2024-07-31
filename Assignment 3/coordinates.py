#Program to check if a set of six numbers is a pair of GPS coordinates
#Fulufhelo Mulaudzi
#05 March 2024

first = int(input("Enter first number:\n"))
second = int(input("Enter second number:\n"))
third = int(input("Enter third number:\n"))
fourth = int(input("Enter fourth number:\n"))
fifth = int(input("Enter fifth number:\n"))
sixth = int(input("Enter sixth number:\n"))

#Use nested if-statements to check if the six number are within the required ranges
#First if checks the latitude and longitude degrees
if (first >= -90 and first <= 90) and (fourth >= -180 and fourth <= 180):
    #Second if checks the minutes
    if (second >= 0 and second <= 59) and (fifth >= 0 and fifth <= 59):
        #Third if checks the seconds
        if (third >= 0 and third <= 59) and (sixth >= 0 and sixth <= 59):
            print("WOW! Looks like geographic coordinates!")
        else:
            print("Hmmm ... looks like 6 random numbers.")
    else:
        print("Hmmm ... looks like 6 random numbers.")
else:
    print("Hmmm ... looks like 6 random numbers.")