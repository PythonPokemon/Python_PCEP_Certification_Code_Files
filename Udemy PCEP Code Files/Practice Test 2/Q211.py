
data = [4, 2, 3, 2, 1]          # Liste mit Zahlen
res = data[0]                   # res = 4 (erstes Element als Startwert)

for d in data:                  # D ie Schleife geht jedes Element d in data der Reihe nach durch.
    if d < res:
        print('d in if:', d)    # 2 -> 1
        res = d                 # Wenn das aktuelle Element d kleiner ist als der bisher kleinste Wert res,
                                # dann wird res auf diesen kleineren Wert gesetzt.

print(res)                      # 1
