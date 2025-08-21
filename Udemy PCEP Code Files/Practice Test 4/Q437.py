"""
data ist eine Liste von Listen (2D-Liste / verschachtelte Liste)
Elemente:

data[0] = [42, 17, 23, 13]
data[1] = [11, 9, 3, 7]
----------------------------------------------------------------
Zusammenfassung

res = data[0][1] → Startwert (zweites Element der ersten Liste)
Doppelte Schleife geht alle Elemente der 2D-Liste durch
if res > d → speichert immer den kleineren Wert
Am Ende → res = kleinster Wert in allen Listen
----------------------------------------------------------------
"""
data = [[42, 17, 23, 13], [11, 9, 3, 7]]
res = data[0][1]    # → zweites Element der ersten Liste == 17
print(res)  # 42

for da in data:
    for d in da:
        if res > d:
            print('d: ', d)  # 17 -> 13 -> 11 -> 9 -> 3
            res = d
print(res)  # 3
