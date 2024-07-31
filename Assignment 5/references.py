#Program to reformat references
#Fulufhelo Mulaudzi
#21 March 2024

#Get the reference input from the user
reference = input("Enter the reference:\n")

#use the find method to find index of first bracket and use that to splice the author name from the reference
first_sep = reference.find("(")
author_names = reference[0:first_sep]       #Splices from first character until just before the first "(" of the year
author_names = author_names.title()         #Uses title method to output name in titlecase

second_sep = reference.find(")") + 2                #Returns index of first letter after the year
third_sep = reference.find(",", second_sep)   #Returns index of first comma after the year

#Splices the title from the input and capitalizes the first letter while leaving the rest as lowercase
title = reference[second_sep:third_sep]
title = title.capitalize()

year = reference[first_sep:second_sep]  #Splices the year from the input
the_rest = reference[third_sep:]        #Splices everything after the title as it is


print("Reformatted reference:")
print(author_names + year + title + the_rest) #Take all of the splices elements and concatenates them together

