"""
Frage 80
Übersprungen
Q162

What is the expected output of the following code?
--------------------------------------------------------------
Richtige Antwort
The program will cause an error

Erklärung:

Die Funktion wird mit beliebigen Parametern definiertfun()
und daher kann sie nicht mit einem Argument aufgerufen werden.
--------------------------------------------------------------
"""


def fun():
    return True


x = fun(False)  # weil hier False übergen wird! | teste ohne false
                # TypeError: fun() takes 0 positional arguments but 1 was given
print(x)
