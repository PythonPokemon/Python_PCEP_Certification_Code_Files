"""
data = set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

set() erstellt eine Menge in Python.
Mengen speichern nur eindeutige Werte → doppelte Einträge werden automatisch entfernt.
Die Reihenfolge ist nicht garantiert (Sets sind ungeordnet).


Darum:
Obwohl die Liste mehrfach 2, 3 und 4 enthält, werden im set nur die eindeutigen Werte {1, 2, 3, 4} gespeichert.
len(data) → 4, weil es nur vier verschiedene Werte gibt.
type(data) → <class 'set'>, zeigt den Datentyp.
"""


data = set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])  # Set = ein Beutel ohne Duplikate, Reihenfolge egal, alles nur einmal drin.
print(len(data))  # länge der einträge == 4 | weil es nur vier verschiedene Werte gibt.

print(type(data))  # <class 'set'> | zeigt den Datentyp.
print(data) # {1, 2, 3, 4}

# Also works directly:
print(len({1, 2, 2, 3, 3, 3, 4, 4, 4, 4}))  # 4

