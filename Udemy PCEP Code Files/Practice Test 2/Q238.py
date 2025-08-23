
data = [[0, 1, 2, 3] for i in range(2)]
# print(data[2][0])  # IndexError: list index out of range

print(data)     # [[0, 1, 2, 3], [0, 1, 2, 3]]
print(data[0])  # [0, 1, 2, 3]
print(data[1])  # [0, 1, 2, 3]

data1 = []                      # erzeugt eine leere list []
for i in range(2):              # i iteriert durch die angegeben listen [[][]]
    data1.append([0, 1, 2, 3])  # fügt der liste data1 werte hinzu, diese wedren direkt den verschachtelten listen zugewiesen
print(data1)                    # [[0, 1, 2, 3], [0, 1, 2, 3]]

