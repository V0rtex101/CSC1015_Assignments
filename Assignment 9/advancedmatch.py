# Program to check if a given pattern matches a given word
# Fulufhelo Mulaudzi
# 24 April 2024

def match(pattern, word):
    """This function takes two arguments: a pattern and a word and then checks
        whether they are a match or not"""

    # First base case: checks if both pattern and word are empty
    if not word and not pattern:
        return True

    # Second base case: checks if one is empty and the other is not
    if not word or not pattern:
        return False

    # Third base case: checks if word is empty and pattern is '*'
    if not word and pattern == '*':
        return True

    # This section makes use of recursion to remove the first char and move on to the next if conditions are satisfied

    # This if checks if it is '*' and then compares the length of the word and pattern
    if pattern[0] == '*':

        if len(word) > 1 and len(pattern) > 1:
            # If second chars of both are equal, remove the first chars
            if pattern[1] == word[1]:
                return match(pattern[1:], word[1:])
            elif pattern[1] == word[0]:
                return match(pattern[1:], word)

        # If the lengths are equal then the first chars are removed and program continues
        if len(word) == len(pattern):
            return match(pattern[1:], word[1:])

        # If word is less than pattern then the first char of pattern is removed
        elif len(word) < len(pattern):
            return match(pattern[1:], word)

        # If the previous conditions are false, the first char of the word is removed until one condition is true
        else:
            return match(pattern, word[1:])

    # This if checks if it is '?' and since it can be any char, it moves on to the next char
    if pattern[0] == '?':
        return match(pattern[1:], word[1:])

    # This if checks if the chars are the same and then moves on to the next char
    elif word[0] == pattern[0]:
        return match(pattern[1:], word[1:])
    return False
