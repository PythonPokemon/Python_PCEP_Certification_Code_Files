"""
Frage 86
Übersprungen
Q421

What is the expected output of the following code?
--------------------------------------------------
Richtige Antwort
14

Erklärung:
Beide Funktionen geben eine string
func1() das string '1'
Und die func2()string '4'

Das ergibt string concatenation'1' + '4''14'
"""


def func1(x):
    return str(x)           # nimmt einen bekibiegen wert und gibt ihn  als string zurück


def func2(x):
    return str(2 * x)       # nimmt einen bekibiegen wert, multipliziert diesen mal zwei und gibt ihn  als string zurück


print(func1(1) + func2(2))  # String wert aus der fun1 == 1 + String wert aus der fun2 == 4 | Ergibt 1 + 4 == 14 Stringkonkatenation
