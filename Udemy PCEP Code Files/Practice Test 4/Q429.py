"""
x ist ein Tuple (unveränderliche Sequenz)
y ist ein Dictionary mit Keys: 2, 4, 6, 8, 10, 12
-------------------------------------------------
res = 1
Startwert der Summe ist 1.
-------------------------------------------------
in der schleife:

for z in x → iteriert über jedes Element des Tuples x
z = 1 → ist nicht in y.keys() → wird übersprungen
z = 4 → ist in y.keys() → res += 4 → res = 5
z = 7 → nicht in y → übersprungen
z = 9 → nicht in y → übersprungen
z = 10 → in y → res += 10 → res = 15
z = 11 → nicht in y → übersprungen
-------------------------------------------------
💡 Merksätze:

in bei einem Dictionary prüft nur die Keys.
Tuple kann man durchiterieren wie eine Liste.
Initialwerte (hier res = 1) werden bei Summen häufig benutzt, z.B. für Offset oder Startwert.
"""

x = (1, 4, 7, 9, 10, 11)    # x ist ein Tuple 
y = {2: 'A', 4: 'B', 6: 'C', 8: 'D', 10: 'E', 12: 'F'}  # y ist ein Dictionary 

res = 1
for z in x:
    print('z in for:', z)
    if z in y:
        # z = 1     → ist nicht in y.keys() → wird übersprungen
        # z = 4     → ist in y.keys() → res += 4 → res = 5
        # z = 7     → nicht in y → übersprungen
        # z = 9     → nicht in y → übersprungen
        # z = 10    → in y → res += 10 → res = 15
        # z = 11    → nicht in y → übersprungen
        print('z in if:', z)
        res += z
print(res)              # 15
