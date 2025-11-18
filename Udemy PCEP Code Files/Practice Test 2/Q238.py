# Erzeugen einer Liste mit verschachtelten Listen
# Jede verschachtelte Liste enthält die Werte 0, 1, 2, 3
# Die äußere Liste enthält 2 dieser verschachtelten Listen

data = [[0, 1, 2, 3] for i in range(2)] # range sagt wie oft die liste wiederholt wird
# print(data[2][0])  # IndexError: list index out of range | <---PRÜFUNGSFRAGE: print(data[2][0]) würde bedeuten, dass es 3 Listen gibt! == [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]

# Listenindex:          0               1
# Elementindex      0  1  2  3    0  1  2  3

print(data)     # [[0, 1, 2, 3], [0, 1, 2, 3]]
print(data[0])  # [0, 1, 2, 3]
print(data[1])  # [0, 1, 2, 3]

print(data[0][3])  # 0 | bedeutet 0  liste und index: 3 == wert 3
print(data[1][1])  # 1 | bedeutet 1  liste und index: 1 == wert 1

