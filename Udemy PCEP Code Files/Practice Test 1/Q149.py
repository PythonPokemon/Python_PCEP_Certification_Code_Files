"""
Detaillierte Erklärung zu ** (Potenzoperator) in Python

1. Was macht **?
** ist der Exponentationsoperator (Potenz).
a ** b bedeutet: "a hoch b", also "a potenziert mit b".

Beispiel:
2 ** 3   |  2 hoch 3 = 2 * 2 * 2 = 8
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
