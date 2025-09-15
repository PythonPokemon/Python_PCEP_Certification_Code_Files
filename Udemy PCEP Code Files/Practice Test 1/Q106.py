"""
Frage 57
Übersprungen
Q106

What is the default return value for a function
that does not explicitly return any value?
-----------------------------------------------
Richtige Antwort
None
"""

def func1():
    pass


print(func1())  # None == „kein Wert“


def func2():
    return


print(func2())  # None

x = None
print(type(x))    # Ausgabe: <class 'NoneType'>