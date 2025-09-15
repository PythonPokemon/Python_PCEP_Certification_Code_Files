"""
Frage 85
Übersprungen
Q403

What is the expected output of the following code?
--------------------------------------------------
Richtige Antwort
16
"""


def func1(a):
    return a ** a


def func2(b):
    # return func1(a) * func1(a)
    # return (a ** a) * (a ** a)
    # return (2 ** 2) * (2 ** 2)
    # return 4 * 4
    return 16

print(func2(2))  # egal was hier als argument übergeben wird die function 2 gibt immer 16 aus, weil in der funktion2 der parameter nicht benutzt wird!
