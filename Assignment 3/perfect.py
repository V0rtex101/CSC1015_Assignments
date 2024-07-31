#Program to determine if a given number is perfect or not
#Fulufhelo Mulaudzi
#05 March 2024

num = int(input("Enter a number:\n"))
count = 0
print(f"The proper divisors of {num} are:")
#Uses a loop to iterate from one up until the input to check for factors
for i in range(1, num):
    if num % i == 0:
        print(i, end=" ")
        count += i
print("\n")
#Serves to check if the sum of the factors add up to the given number to see whether it is perfect or not
if count == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")