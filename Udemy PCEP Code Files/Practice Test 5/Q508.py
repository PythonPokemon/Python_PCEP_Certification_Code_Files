"""
sequence[start:stop:step]

start → Index inklusive (das Element wird mitgenommen)
stop → Index exklusive (das Element wird nicht mehr mitgenommen)
step → Schrittweite (Standard = 1 → jedes Element zwischen start und stop)
--------------------------------------------------------------------------
Negative Indizes → zählen von rechts nach links:
-1 → letztes Element
-2 → vorletztes Element
--------------------------------------------------------------------------
| Index | Wert |
| ----- | ---- |
| 0     | 1    |
| 1     | 2    |
| 2     | 4    |
| 3     | 8    |
----------------    +  Plus Bereich, von links nach rechts   +
----------------      ACHTUNG
----------------    -  Minus Bereich, von rechts nach links -
| -4    | 1    |
| -3    | 2    |
| -2    | 4    |
| -1    | 8    |

"""


data = (1, 2, 4, 8) # Tupel mit 4 elementen
data = data[-2:-1]  # [start:stop:step] == [-2:-1:DEFAULT] | DEFAULT ist standartmäßig 1
print(data)  # (4,)
data = data[-1]
print(data)  # 4
