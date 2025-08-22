"""
int() schneidet nur den Dezimalteil ab (nicht mathematisch runden!)
int(-0.5) → 0
Das ist entscheidend, weil es den Index bestimmt
-------------------------------------------------------------------
💡 Merksatz für Anfänger:

/ liefert float
int() schneidet Dezimalstellen ab
Index 0 greift auf das erste Element in der Liste zu
Deshalb kommt 'Peter' heraus
-------------------------------------------------------------------
"""


#Index     0        1       2
data = ['Peter', 'Paul', 'Mary']
print(data[int(-1 / 2)])  # -1 / 2 == 0,5 | == 0 Peter

print(-1 / 2)     # -0.5
print(int(-0.5))  # 0
