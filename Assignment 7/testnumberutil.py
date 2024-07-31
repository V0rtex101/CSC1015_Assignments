#testnumberutil.py
"""
>>> import numberutil
>>> numberutil.aswords(300)
'three hundred'
>>> numberutil.aswords(0)
'zero'
>>> numberutil.aswords(65)
'sixty five'
>>> numberutil.aswords(15)
'fifteen'
>>> numberutil.aswords(519)
'five hundred and nineteen'
>>> numberutil.aswords(725)
'seven hundred and twenty five'
>>> numberutil.aswords(990)
'nine hundred and ninety'
>>> numberutil.aswords(30)
'thirty'

"""
import doctest
doctest.testmod(verbose=True)