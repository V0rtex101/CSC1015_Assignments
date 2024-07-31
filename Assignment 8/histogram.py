# Program that takes list of marks and outputs a histogram representation of them
# Fulufhelo Mulaudzi
# 15 April 2024

# Get the marks from the user
marks = input("Enter a space-separated list of marks:\n")
marks = marks.split()

# Set empty arrays for each category to act as counters
first = []
upper_second = []
lower_second = []
third = []
fail = []

# Loops through each mark and assigns an 'X' to its corresponding category
for mark in marks:
    mark = int(mark)
    if mark < 50:
        fail.append("X")
    elif 50 <= mark < 60:
        third.append("X")
    elif 60 <= mark < 70:
        lower_second.append("X")
    elif 70 <= mark < 75:
        upper_second.append("X")
    else:
        first.append("X")

# Uses the length of each corresponding array to print out the number of 'X'
print("1 |", "X" * len(first), sep="")
print("2+|","X" * len(upper_second), sep="")
print("2-|", "X" * len(lower_second), sep="")
print("3 |", "X" * len(third), sep="")
print("F |", "X" * len(fail), sep="")
