# Program that asks user for word length and filename the writes words of that length and their anagrams to filename
# Fulufhelo Mulaudzi
# 04 May 2024

from anagramsearch import anagram_finder


def word_finder(length, filename):
    """This function scans a file for words of the given length and returns a list"""
    words = []

    # Scans through the file until "START" is found
    f = open(filename, "r")
    for scan in f:
        if scan == "START\n":
            break

    # Makes a list of all the words found in the file
    file = f.read()
    file = file.split("\n")
    f.close()

    # Checks if the word is the right length and appends to list if true
    for line in file:
        if len(line) == length:
            words.append(line)

    words = sorted(words)
    return words


def set_writer(sets, filename):
    """Function that writes words to a given file name"""
    f = open(filename, "w")
    for words in sets:
        f.write(str(words) + '\n')
    f.close()


def main():
    print("***** Anagram Set Search *****")
    length = int(input("Enter word length:\n"))
    print("Searching...")
    filename = input("Enter file name:\n")
    print("Writing results...")

    final = []
    words_with_length = word_finder(length, "EnglishWords.txt")

    # Checks if the words have anagrams or not then appends the words to a list
    for word in words_with_length:
        temp = [word] + anagram_finder(word, "EnglishWords.txt")
        temp = sorted(temp)
        # Avoids duplication of words
        if temp in final or len(temp) == 1:
            pass
        else:
            final.append(temp)

    set_writer(final, filename)


if __name__ == "__main__":
    main()


