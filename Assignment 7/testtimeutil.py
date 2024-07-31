#testtimeutil.py
"""
>>> import timeutil
>>> timeutil.validate(':15 p.m.')
False
>>> timeutil.validate('003:36 a.m.')
False
>>> timeutil.validate('02:58 a.m.')
False
>>> timeutil.validate('11:21 am')
False
>>> timeutil.validate('10:1 a.m.')
False
>>> timeutil.validate('4:16 p.m.')
True

"""
import doctest
doctest.testmod(verbose=True)