"""
Erklärung Schritt für Schritt:
-----------------------------------------------------------------
range(5, 0, -1)

Startwert: 5
Endwert: 0 (exklusiv → hört bei 1 auf)
Schrittweite: -1 → es wird rückwärts gezählt.
    → erzeugt also die Zahlen: 5, 4, 3, 2, 1
-----------------------------------------------------------------
for i in range(...)
    i nimmt nacheinander die Werte 5, 4, 3, 2, 1 an.
-----------------------------------------------------------------
print(i, i, i, i, i)
    Gibt die aktuelle Zahl i fünfmal aus, getrennt durch Leerzeichen.
-----------------------------------------------------------------
Ausgabe:
5 5 5 5 5
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1

"""

for i in range(5, 0, -1):
    print(i, i, i, i, i)

print('-----')

# for i in range(5, 0, None):   # TypeError: ...| weil schrittweite nicht none sein kann!
#     print(i, i, i, i, i)

print('-----')

# for i in range(5, 0, 0):      # ValueError: ...start 5, ende 0, schrittweite 0 ! | was soll dann gezählt werden?
#     print(i, i, i, i, i)

print('-----')

for i in range(5, 0, 1):
    print(i, i, i, i, i)

print(list(range(5, 0, 1)))     # [] | Da 5 schon größer als 0 ist und der Schritt positiv ist, wird die Bedingung nie erfüllt. 
                                # Ergebnis: leere Liste [].
