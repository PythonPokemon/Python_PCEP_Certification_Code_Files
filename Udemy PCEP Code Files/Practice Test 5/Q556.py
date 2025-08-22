"""
✅ Merksatz

Positionsargumente → zuerst
Keyword-Argumente → danach
Nie positional nach keyword
"""


def func(a, b):
    return b ** a


# print(func(b=2, 2))   # korrekt wäre: print(func(b=2, a=2)) 
# SyntaxError: 

