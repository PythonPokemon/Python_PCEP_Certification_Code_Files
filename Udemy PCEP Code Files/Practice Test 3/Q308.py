"""
Kurzfassung
range() kann sowohl ins Positive als auch ins Negative zählen - es hängt nur vom Startwert, Stopwert und Schritt (step) ab.

Wenn du bei range() keine Schrittweite (step) angibst, wird automatisch 1 genommen.
----------------------------------------------------------------------------------------------
Grundprinzip

range(start, stop, step)

start = Wo das Zählen beginnt
stop = Wo das Zählen aufhört (exklusiv, wird nicht mitgezählt)
step = Wie viel pro Schritt gezählt wird (Standard: +1) oder -1 für rückwährts
----------------------------------------------------------------------------------------------
Positive Richtung

list(range(0, 5))   # [0, 1, 2, 3, 4]
list(range(-2, 3))  # [-2, -1, 0, 1, 2]
start < stop

step muss positiv sein
----------------------------------------------------------------------------------------------
Negative Richtung

list(range(5, 0, -1))   # [5, 4, 3, 2, 1]
list(range(2, -3, -2))  # [2, 0, -2]
start > stop

step muss negativ sein
----------------------------------------------------------------------------------------------
"""


print(len([i for i in range(0, -2)]))      # 0, da python nur automatisch hoch zähl wenn kein step definiert ist, aber nicht ins negative!
print(len([i for i in range(0, -2, -1)]))  # 2 | 0, -1
print(len([i for i in range(-2, 0)]))      # 2 | -2, -1
