"""
data = {} dictionary
key 2: [1,2] wert
key 1: [3,4] wert

das dictionary bekommt also jeweils key mit werten zugewiesen
"""
data = {}
data['2'] = [1, 2]
data['1'] = [3, 4]

for i in data.keys():           # i iteriert duch data's keys
    print(data[i][1], end=' ')  # ausgabe aus data in i jeweils dd

print()
print(data)  # {'2': [1, 2], '1': [3, 4]}
