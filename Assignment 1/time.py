# Program to convert an amount of minutes into an equivalent amount 
# of days, hours and minutes.
#
# Name: Stephan Jamieson
#

#Get number of minutes from the user
input_str = input("Enter a quantity of minutes: ")
minutes = int(input_str)

#Convert the minutes into days, hours and minutes
hours = minutes//60
days = hours//24
minutes = minutes%60
hours = hours%24

#Display the output
print("The number of days is", days, end=', ')
print("the number hours is", hours, end=', ')
print("and the number of minutes is", minutes, end='')
print(".")
