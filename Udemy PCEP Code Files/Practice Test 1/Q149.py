"""
Frage 208
Übersprungen
Q149
Which of the following statements are true?
(Select two answers)

Richtige Auswahl
The ** operator uses right-sided binding.
Erklärung
The ** operator in Python uses right-sided binding, meaning that when there are multiple ** operators in an expression, the rightmost one is evaluated first. This is important to consider when working with exponentiation operations in Python.

Richtige Auswahl
The right argument of the % operator cannot be zero.
Erklärung
In Python, when using the % operator for the modulo operation, the right argument (the divisor) cannot be zero. Attempting to perform modulo division by zero will result in a ZeroDivisionError.

---------------------------------------------------------------
Schritt-für-Schritt Auswertung von 4 ** 3 ** 2

1.Zuerst den rechten Teil berechnen: 3 ** 2
→ 3 hoch 2 = 9

2.Dann die Potenzierung mit dem Ergebnis: 4 ** 9

3.Was ist 4 hoch 9?
4 ** 9 heißt:
4 * 4 * 4 * 4 * 4 * 4 * 4 * 4 * 4

Rechne das aus:

4² = 16
4³ = 64
4⁴ = 256
4⁵ = 1024
4⁶ = 4096
4⁷ = 16384
4⁸ = 65536
4⁹ = 262144
"""


print(4 ** 3 ** 2)    # 262144
print(4 ** (3 ** 2))  # 262144
print(4 ** 9)         # 262144
print(262144)         # 262144

# print(7 % 0)  # ZeroDivisionError
