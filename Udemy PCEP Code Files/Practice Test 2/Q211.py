"""
Ablauf Schritt für Schritt:

res = 4

       vergleich d   res
                 |   |
d = 4  vergleich 4 < 4 ❌ → nichts passiert
d = 2  vergleich 2 < 4 ✅ → res = 2
d = 3  vergleich 3 < 2 ❌ → nichts passiert
d = 2  vergleich 2 < 2 ❌ → nichts passiert
d = 1  vergleich 1 < 2 ✅ → res = 1

👉 Am Ende: res = 1
"""

data = [4, 2, 3, 2, 1]      # Liste mit Zahlen
res = data[0]               # res = 4 (erstes Element als Startwert)

for d in data:              # Schleife: d nimmt nacheinander die Werte 4, 2, 3, 2, 1 an
    if d < res:             # Prüfen: ist d kleiner als der aktuelle Wert in res?
        print('d in if:', d)  # Wird nur ausgeführt, wenn Bedingung wahr ist
        res = d             # res bekommt den neuen kleineren Wert

print(res)                  # Ausgabe: 1 (kleinster Wert in der Liste)
# Ausgabe der Zwischenschritte:
# d in if: 2
# d in if: 1
# 1