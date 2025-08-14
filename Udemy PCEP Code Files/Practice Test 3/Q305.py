"""
Kurzfassung
Der Code erstellt eine 2D-Liste (data) mit drei gleichen Zeilen: [3, 2, 1].
Anschließend wird die Diagonale dieser Liste ausgelesen (3, 2, 1) und addiert.
Ergebnis: 6.
"""


data = [[3-i for i in range(3)] for j in range(3)]
print(data)  # [[3, 2, 1], [3, 2, 1], [3, 2, 1]]
res = 0

for i in range(3):
    print('data[' + str(i) + '][' + str(i) + ']: ', data[i][i])
    """
    data[0][0]: 3
    data[1][1]: 2
    data[2][2]: 1
    """
    res += data[i][i]

print(res)  # Ausgabe: 6, weil 3 + 2 + 1 = 6
