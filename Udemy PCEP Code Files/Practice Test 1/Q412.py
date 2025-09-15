"""
Frage 34
Übersprungen
Q412

An operator able to check whether two values are equal, is coded as:

Richtige Antwort
==

"""


print(23 == 23)     # True | → Prüft, ob die Werte gleich sind.

# print(23 === 23)  # SyntaxError: invalid syntax

w = 42              # The is to assign values.assign operator=

x = ['Peter']
y = ['Peter']
print(x is y)       # False | → is prüft, ob beide Variablen auf dasselbe Objekt im Speicher zeigen.

print(id(x))        # 2013859176640
print(id(y))        # 2013859325504

"""
----------------------------------------------------------------------
→ is prüft, ob beide Variablen auf dasselbe Objekt im Speicher zeigen.
x und y enthalten zwar die gleichen Werte (['Peter']),

aber Python erzeugt zwei verschiedene Listen im Speicher.
Deshalb sind x == y True, aber x is y False.
----------------------------------------------------------------------
"""