# Program to search a file for anagrams of a given word
# Fulufhelo Mulaudzi
# 03 May 2024

import os.path


def anagram_finder(word, filename):
    """Function that takes two string arguments: a word and name of the file.
     It searches the file for anagrams of the given word and returns a list"""
    dic = {}
    word_dic = {}
    results = []

    # Makes a dictionary of the letters of the given word
    for char in word:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1

    # Opens the file and goes through it until it reaches "START"
    f = open(filename, "r")
    for scan in f:
        if scan == "START\n":
            break

    # Takes all the words it finds in the file and makes them into a list
    file = f.read()
    file = file.split("\n")
    f.close()

    # Iterates through each word and makes a dictionary of its letters
    for w in file:
        for char in w:
            if char in word_dic:
                word_dic[char] += 1
            else:
                word_dic[char] = 1

        # Checks if the word is an anagram of the input word then appends it to results if true
        if word_dic == dic and w != word:
            results.append(w)
        word_dic = {}

    results = sorted(results)
    return results


def main():
    print("***** Anagram Finder *****")

    # Checks if the file exists or not
    if os.path.isfile("EnglishWords.txt"):
        user = input("Enter a word:\n")
        user = user.lower()

        # Checks if the anagram_finder function returns an empty string or not
        if anagram_finder(user, "EnglishWords.txt"):
            print((anagram_finder(user, "EnglishWords.txt")))
        else:
            print(f"Sorry, anagrams of '{user}' could not be found.")

    else:
        print("Sorry, could not find file 'EnglishWords.txt'.")


if __name__ == "__main__":
    main()
