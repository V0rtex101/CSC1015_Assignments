#Program to convert format of date and time
#Fulufhelo Mulaudzi
#22 March 2024

initial = input("Enter the date and time (yyyy-mm-dd hh:mm):\n")

#Splices the different parts of the input into the appropriate variables
time = int(initial[11:13])
day = int(initial[8:10])
month = int(initial[5:7])
year = (initial[2:4])

#Uses if-statements to check whether the time is am or pm
if time < 12 and time != 0:
    t = str(time) + initial[13:16] + " am"
elif time == 0:
    t = "12" + initial[13:16] + " am"
elif time > 12:
    t = str(time - 12) + initial[13:16] + " pm"
else:
    t = str(time) + initial[13:16] + " pm"

#Uses if-statements to check what suffix should follow the day of the month
if day % 10 == 1 and not 10 < day < 20:
    d = str(day) + "st"
elif day % 10 == 2 and not 10 <day <20:
    d = str(day) + "nd"
elif day % 10 == 3 and not 10 <day< 20:
    d = str(day) + "rd"
else:
    d = str(day) + "th"

#Uses if-statements to output the appropriate month name
if month == 1:
    m = "January"
elif month == 2:
    m = "February"
elif month == 3:
    m = "March"
elif month == 4:
    m = "April"
elif month == 5:
    m = "May"
elif month == 6:
    m = "June"
elif month == 7:
    m = "July"
elif month == 8:
    m = "August"
elif month == 9:
    m = "September"
elif month == 10:
    m = "October"
elif month == 11:
    m = "November"
else:
    m = "December"

#Adds a single quote to the last 2 digits of the year
y = "'" + year

print(t, "on the", d, "of", m, y)