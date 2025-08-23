"""
-----------------------------------------------------------
Das ist eine verschachtelte Listen-Komprehension.
for y in range(3) → y nimmt die Werte 0, 1, 2 an.
Für jedes y wird eine Liste [x for x in range(y)] erstellt.
-----------------------------------------------------------
🔎 Details:

Wenn y = 0: range(0) → keine Werte → []
Wenn y = 1: range(1) → [0]
Wenn y = 2: range(2) → [0, 1]
-----------------------------------------------------------
➡ Ergebnis:

data = [[], [0], [0, 1]]
-----------------------------------------------------------
"""
data = [[x for x in range(y)] for y in range(3)]
print(data)         # [[], [0], [0, 1]]

for d in data:
    print('d:', d)  # [] -> [0] -> [0, 1]
    if len(d) < 2:
        print('*')  # * *

print(range(0))  # range(0, 0)
print(bool(range(0)))  # False




