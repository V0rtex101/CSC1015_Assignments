# Program to print out calendar for a given month
# Fulufhelo Mulaudzi
# 03 April 2024

from math import floor


def day_of_week(day, month, year):
    # Takes the date of a certain day then returns the day that date lies on. 1 for Monday up until 7 for Sunday

    if month == 1 or month == 2:
        month += 12
        year -= 1
    h = (day + floor(13 * (month + 1)) / 5 + year + floor(year / 4) - floor(year / 100) + floor(year / 400)) % 7
    output = ((h + 5) % 7) + 1
    return int(output)


def is_leap(year):
    # Checks whether the year is a leap year or not and then returns a boolean value

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


def month_num(month_name):
    # It takes a given month and return the number associated with it. 1 for January up until 12 for December

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    if month_name.title() in months:
        return months.index(month_name.title()) + 1


def num_days_in(month_num, year):
    # It takes a given month and returns the number of days in that month and also accounts for leap years

    if month_num in [4, 6, 9, 11]:
        return 30
    elif month_num in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month_num == 2 and is_leap(year):
        return 29
    else:
        return 28


def num_weeks(month_num, year):
    # Determines the number of weeks using the number of days in the month and the day the month begins

    if num_days_in(month_num, year) == 31 and day_of_week(1, month_num, year) > 5:
        return 6
    elif num_days_in(month_num, year) == 31 and day_of_week(1, month_num, year) <= 5:
        return 5
    elif num_days_in(month_num, year) == 30 and day_of_week(1, month_num, year) == 7:
        return 6
    elif num_days_in(month_num, year) == 30 and day_of_week(1, month_num, year) < 7:
        return 5
    elif num_days_in(month_num, year) == 28 and day_of_week(1, month_num, year) == 1:
        return 4
    elif num_days_in(month_num, year) == 28 and day_of_week(1, month_num, year) > 1:
        return 5
    elif num_days_in(month_num, year) == 29 and day_of_week(1, month_num, year) == 7:
        return 6
    else:
        return 5


def week(week_num, start_day, days_in_month):
    """It outputs the given week of a month.
    A dictionary is used to store the values of each week
    The odd days are calculated and spaces are used to fill them before the
    starting day of the month. The for loop then adds values to each week depending on if all
    seven slots of the previous week have been filled before filling the next one.
    Finally, the function output the week as a string.
    """
    weeks = {1: "", 2: "", 3: "", 4: "", 5: "", 6: ""}
    j = 1
    odd_days = start_day - 2
    space = ''
    space = space.rjust(2, ' ')
    for i in range(days_in_month + odd_days + 1):
        if i <= odd_days:
            weeks[j] += space + ' '
        else:
            weeks[j] += "{0:2d}".format(i - odd_days) + ' '
            if (i + 1) % 7 == 0:
                j += 1

    return weeks[week_num]


def main():
    m = input("Enter month:\n")
    y = int(input("Enter year:\n"))
    print(m.title())
    print("Mo Tu We Th Fr Sa Su")

    num_of_weeks = num_weeks(month_num(m), y)
    first_day = day_of_week(1, month_num(m), y)
    num_of_days = num_days_in(month_num(m), y)
    # This for loop serves to print out the weeks of the month depending on the number of weeks it has
    for w in range(1, num_of_weeks + 1):
        print(week(w, first_day, num_of_days))


if __name__ == '__main__':
    main()
