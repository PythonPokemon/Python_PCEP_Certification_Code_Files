"""
data = {} dictionary

IndexWert:          
        0  1
key 2: [1, 2] wert
key 1: [3, 4] wert

das dictionary bekommt also jeweils key mit werten zugewiesen
"""
data = {}
data['2'] = [1, 2]
data['1'] = [3, 4]

for i in data.keys():           # i iteriert duch data's keys
    print(data[i][1], end=' ')  # ausgabe der Key/Value's explizit aus Index[1], aber hintereinander, wegen dem ausdruck: end=' ' == 24

print()
print(data)  # {'2': [1, 2], '1': [3, 4]}
