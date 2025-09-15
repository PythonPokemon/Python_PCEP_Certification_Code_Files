"""
Frage 67
Übersprungen
Q256

Which of the following lines properly starts a function using two parameters,
both with zeroed default values?
-----------------------------------------------------------------------------
Richtige Antwort
def fun(a=0, b=0):
"""


def fun(a=0, b=0):
    print(a, b)


fun()  # 0 0


def fun(a, b=0):
    print(a, b)


fun()  # TypeError: fun() missing 1 required positional argument: 'a'

# def fun(a=0, b): print(a, b)
# SyntaxError: non-default argument follows default argument

# def fun(a=b=0): print(a, b)
# SyntaxError: invalid syntax
