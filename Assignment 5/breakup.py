#Program that outputs a given sentence as a comma-seperated list of lowercase letters
#Fulufhelo Mulaudzi
#23 March 2024

sentence = input("Enter a sentence:\n")
count = sentence.count(" ")
output = ""

#Use for loop to iterate through the sentence using number of spaces
for i in range(0, count + 1):
    space_index = sentence.find(" ")
    if space_index != -1:            #Extracts each word from the input and puts a comma after it
        output += sentence[0:space_index] + ", "
        sentence = sentence[space_index + 1:]

    else:                    #Happens on last word and adds it to output variable and puts a full stop at the end
        output += sentence + "."

final = output.lower() #makes all the the letters lowercase
print("The word list:", final)