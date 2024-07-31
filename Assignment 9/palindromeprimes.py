# Program that uses recursive functions to find all palindromic primes between two integers
# Fulufhelo Mulaudzi
# 25 April 2024

from palindrome import palindrome
import sys
sys.setrecursionlimit(30000)


def prime(n, divisor=2):
    """This function checks whether a given number is a prime number or not."""
    # Base case of 2 since it is a prime
    if n == 2:
        return True
    # Checks if it is divisible by a number other than 1
    if n % divisor == 0:
        return False
    # Checks if the function has reached the square root and returns True
    if divisor * divisor > n:
        return True
    return prime(n, divisor + 1)


def palindrome_primes(n, m):
    """This function outputs prime palindromes in the given interval"""
    # Checks if function has reached end interval to terminate program
    if n > m:
        return
    # Checks if n is 2 and prints it out since it is a palindromic prime
    if n == 2:
        print(n)
    # Checks if n is even and moves to next odd num since even numbers aren't primes except only 2
    if n % 2 == 0:
        n += 1
    num_str = str(n)
    # Checks it num is a prime palindrome and prints it out
    if palindrome(num_str, 0, len(num_str)-1) and prime(n):
        print(n)

    return palindrome_primes(n + 2, m)


def main():
    start = int(input("Enter the starting point N:\n"))
    end = int(input("Enter the ending point M:\n"))

    print("The palindromic primes are:")
    palindrome_primes(start, end)


if __name__ == "__main__":
    main()
