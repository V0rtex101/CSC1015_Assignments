#Program to print sequence of 7 numbers, starting from input value
#Fulufhelo Mulaudzi
#14 March 2024

num = int(input("Enter a number between -6 and 93:\n"))

#Checks if the input is within the given range
if num > -6 and num < 93:

    #Iterates through the range and ensures that all the values are two digits
    for i in range(num, num + 7):
        if i < 10 and i >= 0:
            print(" ", i, sep="", end=" ")
        else:
            print(i, end=" ")
else:
    print("Invalid input! The value of \'n\' should be between -6 and 93.")

