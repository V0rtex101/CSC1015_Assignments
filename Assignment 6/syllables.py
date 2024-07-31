# Program that if given a word, calculates how many syllables it contains.
# Fulufhelo Mulaudzi
# 03 April 2024

def is_vowel(letter):
    # This function checks whether a character entered is a vowel or not then returns a boolean value
    if letter in "aeiouy":
        return True
    else:
        return False


def count_syllables(word):
    # This function counts how many syllables are in the word entered.
    count = 0
    prev_is_vowel = False
    for letter in word.lower():
        if is_vowel(letter):
            count += 1
            if prev_is_vowel:   # Checks to see if two vowels follow each other so that they are counted as 1 syllable
                count -= 1
            prev_is_vowel = True
        else:
            prev_is_vowel = False

    # Checks to see if word ends with 'e' to not count in as a syllable except if it is the only vowel in the word
    if word.endswith('e') and count > 0 and not is_vowel(word[-2]):
        count -= 1

    return max(count, 1)        # Ensures that at least a syllable of 1 is returned


def main():
    ask = True
    while ask:
        word = input('Enter a word (or \'q\' to quit):\n')
        if word != 'q':
            num_of_syllables = count_syllables(word)
            if num_of_syllables > 1:
                print(f"The word '{word}' has {num_of_syllables} syllables.\n")
            else:
                print(f"The word '{word}' has {num_of_syllables} syllable.\n")
        else:
            ask = False


# Do not modify.
if __name__ == '__main__':
    main()
