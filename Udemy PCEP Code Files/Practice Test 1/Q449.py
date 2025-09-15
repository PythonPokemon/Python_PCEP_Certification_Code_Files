"""
Frage 120
Übersprungen
Q449

What will be the output of the following snippet?

a = 1
b = 0
a = a ^ b
b = a ^ b
b = a ^ b
print(a, b)

---------------------------------------------------------------------

Richtige Antwort
1 0
---------------------------------------------------------------------
Bedeutung

^ in Python ist der bitweise XOR-Operator.
XOR = exclusive OR = exklusives ODER.
Regel: Das Ergebnis ist 1, wenn genau einer von beiden 1 ist.
Wenn beide gleich sind (beide 0 oder beide 1) → Ergebnis 0.

Wahrheitstabelle XOR
-----------------
| a | b | a ^ b |
| - | - | ----- |
| 0 | 0 |   0   |
| 0 | 1 |   1   |
| 1 | 0 |   1   |
| 1 | 1 |   0   |
-----------------

"""


print(0 ^ 0)  # 0
print(0 ^ 1)  # 1
print(1 ^ 0)  # 1
print(1 ^ 1)  # 0

