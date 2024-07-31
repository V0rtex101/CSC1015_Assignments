#testpalindrome.py
"""
>>> import palindrome
>>> palindrome.palindrome('')
True
>>> palindrome.palindrome('f')
True
>>> palindrome.palindrome('52645')
False
>>> palindrome.palindrome('step on no pets')
True
>>> palindrome.palindrome('Ava')
False

"""
import doctest
doctest.testmod(verbose=True)