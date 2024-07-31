#Program to print out every 7th number in the range from n to n+41
#Fulufhelo Mulaudzi
#14 March 2024

num = int(input("Enter a number between -6 and 2:\n"))

#Checks that the input is within the given range
if num > -6 and num < 2:
    for i in range(num, num + 41, 7):
        if i < 10 and i >= 0:
            print(" ", i, sep="")
        else:
            print(i)
else:
    print("Invalid input! The value of \'n\' should be between -6 and 2.")