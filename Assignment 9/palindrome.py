# Program that uses recursion to check for a palindrome
# Fulufhelo Mulaudzi
# 23 April 2024

def palindrome(string, start_left, start_right):
    s = string.strip()  # Removes any leading whitespaces

    # Checks if the left and right index trackers are on the same position or have passed each other
    if start_left >= start_right:
        return True
    # Checks if the chars pairs are the same and then moves over to the next pair
    elif s[start_left] == s[start_right]:
        return palindrome(string, start_left + 1, start_right - 1)

    return False


def main():
    response = input("Enter a string:\n")
    if palindrome(response, 0, len(response) - 1):
        print("Palindrome!")
    else:
        print("Not a palindrome!")


if __name__ == "__main__":
    main()
