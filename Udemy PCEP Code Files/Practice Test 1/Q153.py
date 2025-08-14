
dct = {}            # Ein leeres Dictionary wird erstellt.
dct['1'] = (1, 2)   # Schlüssel '1' bekommt den Wert (1, 2) (ein Tupel).
dct['2'] = (2, 1)   # Schlüssel '2' bekommt den Wert (2, 1) (ebenfalls ein Tupel)
print(dct)  # {'1': (1, 2), '2': (2, 1)}

for x in dct.keys():

    print(dct[x][1], end='')  # x holt den wert aus der variable 'dct' auf dem index[1] ==  21

print()
print(dct['1'][1])  # gibt den wert von schlüssel 1, index 1 aus == 2
print(dct['2'][1])  # gibt den wert von schlüssel 1, index 1 aus == 1

print((1, 2)[1])  # 2
print((2, 1)[1])  # 1
