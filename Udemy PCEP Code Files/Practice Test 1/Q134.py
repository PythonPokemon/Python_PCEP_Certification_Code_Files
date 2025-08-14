"""
.insert(index, wert) in Python

Funktion: Fügt einen Wert an einer bestimmten Position (Index) in die Liste ein.
Index: Die Position, an der der Wert eingefügt wird (0 = ganz vorne).
Bestehende Elemente werden nach hinten verschoben – nichts wird gelöscht.
"""
x = [0, 1, 2]
x.insert(1, 4) # fügt vor Index 1 die Zahl '4' ein, sodass sich alles nach rechts verschiebt! [0, -> 4 <-, 1, 2]
print(x)       # [0, 4, 1, 2]
print("länge des index ist: "+ str(len(x)))

del x[1]
print(x)       # [1, 1, 2]
print(sum(x))  # 4
