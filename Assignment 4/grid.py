#Program to print out a grid of numbers from user input
#Fulufhelo Mulaudzi
#14 March 2024

num = int(input("Enter a number between -6 and 2:\n"))

if num > -6 and num < 2:

    #responsible for the numbers in the first column
    for i in range(num, num + 41, 7):

        #prints the numbers in each row
        for j in range(i, i + 7):
            if j < 10 and j >= 0:
                print(" ", j, sep="", end=" ")
            else:
                print(j, end=" ")
        print("")
else:
    print("Invalid input! The value of \'n\' should be between -6 and 2.")