"""
Lösungsmöglichkeiten
Tuple in Liste umwandeln, ändern, zurückwandeln
------------------------------------------------------------------------------------------------------------
data = list(data)  # Tuple → Liste
data[0] = 2        # Änderung möglich
data = tuple(data) # Liste → Tuple zurück
print(data)        # (2, 1, 
------------------------------------------------------------------------------------------------------------
Mini-Erklärung 
Tuples sind wie Listen, aber unveränderlich. 
Das bedeutet: Man kann keine Elemente ändern. 
Wenn du ein Element ersetzen willst, musst du entweder eine Liste daraus machen oder ein neues Tuple bauen.“
------------------------------------------------------------------------------------------------------------
"""


data = (1,) * 3 # Erzeugt ein Tuple mit drei Einsen: (1, 1, 1)
data[0] = 2     # TypeError: ...Tuples sind immutable → kein append, pop oder Zuweisung an Index möglich
print(data)
