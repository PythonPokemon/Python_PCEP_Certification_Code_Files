"""
1️⃣ Unterschied: Slice vs. range()
--------------------------------------------------------------
a) Slice-Syntax [start:end:step]
    Wird bei Listen, Tupeln oder Strings verwendet
    Beispiel:

my_list = [0, 1, 2, 3, 4]
print(my_list[1:4:2])  # [1, 3]

    start:end:step → Drei Teile durch Doppelpunkte getrennt
--------------------------------------------------------------
b) range(start, stop[, step])
    Wird bei for-Schleifen verwendet
    Syntax: range(start, stop) oder range(start, stop, step)
    Keine Doppelpunkte, sondern Kommas
    Beispiel:

for i in range(-1, 1):
    print(i)

    Start = -1, Stop = 1, Schritt = 1 (Standard)
    Iteriert über i = -1, 0
--------------------------------------------------------------
for i in range(-1, 1):
Das ist keine Slice-Notation

Der Doppelpunkt, den du meinst, 
gibt es hier nicht → Komma trennt die Argumente

Python weiß: range(start=-1, stop=1, step=1)
--------------------------------------------------------------
💡 Merksatz

: → Slice

, → Parameterliste (z.B. range(start, stop, step))
--------------------------------------------------------------
"""


for i in range(-1, 1):  # start(inklusiv) -1, 0, ende(exclusiv) | bleibt stehen 1 
    print("*")
    # * | -1
    # * | 0 bleibt hier stehen!
    # * | 1

for i in range(-1, 1):
    print(i)
    # -1
    # 0
