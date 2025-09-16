"""
 bei Tuples suchst du immer nach dem Positions/Wert, nicht nach einem Index.
"""
#Index 0  1  2
foo = (1, 2, 3,) # Tuple mit 3 Werten

print(foo.index(1)) # 0 | .index(x) sucht nach dem Wert x und gibt den Index zurück, an dem dieser Wert das erste Mal steht.
print(foo.index(2)) # 1 | foo.index(WERT) → Suche nach WERT, Ergebnis ist der Index.
print(foo.index(3)) # 2 | foo.index(WERT) → Suche nach WERT, Ergebnis ist der Index.

#foo.index(0)       # ❌ Fehler: 0 ist kein Wert im Tupel | # ValueError: tuple.index(x)


print(foo[0])       # foo[INDEX] → Suche nach INDEX, Ergebnis ist der Wert. == 1
print(foo[1])       # foo[INDEX] → Suche nach INDEX, Ergebnis ist der Wert. == 2
print(foo[2])       # foo[INDEX] → Suche nach INDEX, Ergebnis ist der Wert. == 3