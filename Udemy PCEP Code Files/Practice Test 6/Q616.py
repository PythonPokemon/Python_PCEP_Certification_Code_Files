"""
listen in einer liste:
2D Array
data = [
                  Spalte
                 j  j  j
                 0  1  2
                 |  |  |
Zeile   i   0   [0, 1, 2],
Zeile   i   1   [0, 1, 2],
Zeile   i   2   [0, 1, 2]

]
"""
#Schleife: Innen → [0, 1, 2]  Außen → [0, 1, 2]
data = [[x for x in range(3)] for y in range(3)]    # Warum nur von [0, 1, 2] gezählt wird, weil die reichweite: range(3) ist!

# Listenanzahl:    |          |          |      == ||| == 3
print(data) # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
for i in range(3):      # i geht über die Zeilen: 0,1,2
    for j in range(3):  # j geht über die Spalten: 0,1,2
        if data[i][j] % 2 != 0: # Prüft, ob das Element ungerade ist (% 2 != 0) | Ungerade Werte in data sind: 1, 1, 1 (einmal pro Zeile)
            print('*')  # deshalb jeweils ein stern pro durchlauf
            # *
            # *
            # *
