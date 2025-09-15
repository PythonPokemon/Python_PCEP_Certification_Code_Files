"""
Frage 123
Übersprungen
Q562

What is the expected output of the following code?

---------------------------------------------------------------------
Richtige Antwort
6
---------------------------------------------------------------------

"""


def fun():
    return 3            # gibt 3 zurück


def add(n):
    return fun() + n    # funktion mit parameter gibt unterfunktion zurück  3 + n(parameter) die sich selbst addiert


print(add(3))  # 3 + 3 = 6
