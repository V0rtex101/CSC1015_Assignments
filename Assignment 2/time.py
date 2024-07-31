#Program to check the validty of time entered from user
#Fulufhelo Mulaudzi
#28 February 2024

hours = int(input("Enter the hours:\n"))
minutes = int(input("Enter the minutes:\n"))
seconds = int(input("Enter the seconds:\n"))

#Use nested if-statements to verify whether the input is valid
if hours >= 0 and hours < 24:
    if minutes >= 0 and minutes < 60:
        if seconds >= 0 and seconds < 60:
            print("Your time is valid.")
        else:
            print("Your time is invalid.")
    else:
        print("Your time is invalid.")
else:
    print("Your time is invalid.")
