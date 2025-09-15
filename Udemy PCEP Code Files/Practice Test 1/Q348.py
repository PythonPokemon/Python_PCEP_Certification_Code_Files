"""
Frage 64
Übersprungen
Q348

Right-sided binding means that the following expression

1 ** 2 ** 3

will be evaluated:
---------------------------------------------------------------------------------------------------------------------------------------------
Richtige Antwort
from right to left

Erklärung
In Python schreibt die rechtsseitige Bindungsregel vor, dass der Potenzierungsoperator (**) von rechts nach links ausgewertet wird. 
Das bedeutet, dass im Ausdruck 1 ** 2 ** 3 die Berechnung damit beginnt, zuerst 2 ** 3 auszuwerten, gefolgt von 1 ** das Ergebnis von 2 ** 3.
---------------------------------------------------------------------------------------------------------------------------------------------
"""


print(1 ** 2 ** 3)    # 1
print(1 ** (2 ** 3))  # 1
print(1 ** 8)         # 1
print(1)              # 1
