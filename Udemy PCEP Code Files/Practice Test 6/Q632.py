"""
Das ist eine rekursive Funktion.

Rekursiv bedeutet: Die Funktion ruft sich selbst auf.
Basisfall: if x == 0: return 0 → Stoppt die Rekursion.
Rekursiver Fall: return x + func(x - 1) → summiert den aktuellen Wert x mit dem Ergebnis von func(x-1).
-------------------------------------------------------------------------------------------------------
Ablauf für func(3)

Wir rufen func(3) auf. Schritt für Schritt:

func(3) → 3 + func(2)
func(2) → 2 + func(1)
func(1) → 1 + func(0)
func(0) → 0  # Basisfall
-------------------------------------------------------------------------------------------------------
Jetzt summieren wir von innen nach außen:

zahl von dem parameter
     |
     |
     |----|
func(1) → 1 + 0 = 1
               ---| plus addition des vorherigen ergebnisses
              |
func(2) → 2 + 1 = 3
               ---| plus addition des vorherigen ergebnisses
              |
func(3) → 3 + 3 = 6
               ---| plus addition des vorherigen ergebnisses
              |
func(4) → 4 + 6 = 10
               ---| plus addition des vorherigen ergebnisses
              |
func(5) → 5 + 10 = 15
-------------------------------------------------------------------------------------------------------
"""


def func(x):
    if x == 0:
        return 0
    return x + func(x - 1)  # 3 + 2 + 1 + 0


print(func(3))  # 6


