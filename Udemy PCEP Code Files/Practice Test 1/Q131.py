"""
🎯 Der entscheidende Unterschied
Integers → unveränderlich → Änderung innerhalb der Funktion wirkt nicht auf die ursprüngliche Variable.
Listen → veränderlich → Änderungen am Inhalt wirken auch außerhalb der Funktion.

Wenn du vor dem Funktionsaufruf x = 4 setzt, hat das mit der Funktionslogik nichts zu tun
 — du änderst x einfach vorher.
 ------------------------------------------------------------------------------------------------------
 Mit andere worten gesagt, x in der globalen Ebene ist nicht das gleiche wie p1 in der Funktion.
 Und deshlab in der funktion p1 = 1 ändert nur die lokale Variable p1, nicht die globale Variable x.
 also in der Funktion wird p1 = 1 gesetzt, aber x bleibt 3.
 weil Integer unveränderlich (immutable) ist.
"""


#-------------Funktions scope-------------
def func(p1, p2):
    p1 = 1        # ändert nur die lokale Variable p1, deshalb ist x immer noch 3 | ausgegraut!
    p2[0] = 42    # greift auf die Liste zu und ändert den wert an Index 0, auf 42
#-------------Funktions scope-------------


#-------------Globaler scope-------------
x = 3           # Integer → unveränderlich (immutable).
y = [1, 2, 3]   # Liste → veränderlich (mutable).
#-------------Globaler scope-------------

# aufruf ohne vorher die funktion zu triggern
print(x, y[0],y[1],y[2])  # x == 3 und y index[0] == 1

# Funktionsaufruf: def func(p1, p2):
func(x, y)

print(x, y[0])



