# Program to check if a given pattern matches a given word
# Fulufhelo Mulaudzi
# 23 April 2024

def match(pattern, word):
    """This function takes two arguments: a pattern and a word and then checks
    whether they are a match or not"""

    # First base case: checks if both pattern and word are empty
    if not word and not pattern:
        return True

    # Second base case: checks if one is empty and the other is not
    if not word or not pattern:
        return False

    # This section makes use of recursion to remove the first char and move on to the next if conditions are satisfied

    # This if checks if it is '?' and since it can be any char, it moves on to the next char
    if pattern[0] == '?':
        return match(pattern[1:], word[1:])

    # This if checks if the chars are the same and then moves on to the next char
    elif word[0] == pattern[0]:
        return match(pattern[1:], word[1:])

    return False
