#Program to translate a sentence into pig latin
#Fulufhelo Mulaudzi
#23 March 2024

sentence = input("Enter a sentence:\n")
count = sentence.count(" ")
new_sen = ""

#This first for loop is meant to iterate over the input sentence using the number of spaces
for i in range(0, count + 1):
    space_index = sentence.find(" ")

    #This if-statement extracts a word from the input depending on the number of words left in the sentence
    if space_index != -1:
        word = sentence[0:space_index]
    else:
        word = sentence[0:]

    #If the first letter of the word is a vowel only "way" will be added to the end of the word
    if word[0] in "aeiou":
        word += "way"

    #This else-statement deals with words which begin with consonants
    else:
        temp_con = ""           #A temporary variable to store the sequence of the beginning consonants
        temp_vow = word         #A temporary variable to store the remaining letters

        #This for loop iterates over the extracted word
        for j in range(0, len(word)):
            if word[j] not in "aeiou":
                temp_con += word[j]     #Sequence of consonants are added to the temporary variable
                temp_vow = temp_vow[1:]
            else:
                break
        word = temp_vow + 'a' + temp_con + 'ay'

    new_sen += word + " "
    sentence = sentence[space_index+1:] #Removes the first word from the input sentence

new_sen = new_sen.lower()
print(new_sen)

