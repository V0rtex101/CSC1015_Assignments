#Program to determine whether a year is a leap year or not
#Fulufhelo Mulaudzi
#28 February 2024

year = int(input("Enter a year:\n"))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")