"""
Frage 98
Übersprungen
Q156

What is the output of the following snippet?
--------------------------------------------
Richtige Antwort
9

"""


def fun(x, y, z):            # Funktion mit drei Parametern x, y, z
    return x + 2 * y + 3 * z # Berechnung: x + (2*y) + (3*z)

print(fun(0, z=1, y=3))      # Aufruf: x=0, y=3, z=1
                             # => 0 + 2*3 + 3*1
                             # => 0 + 6 + 3
                             # => 9


print(0 + 2 * 3 + 3 * 1)      # 9 | 0 + 6 + 3 == 9
print(0 + (2 * 3) + (3 * 1))  # 9
print(0 + 6 + (3 * 1))        # 9
print(0 + 6 + 3)              # 9
print(6 + 3)                  # 9
print(9)                      # 9
