# startwert 1, schreitweite 6, bedeutet maximal 5 Werte
for i in range(1, 6):
    print(str(i) * 5)   # gibt 5 mal den Wert von i aus
"""
11111
22222
33333
44444
55555
"""

print('----------')

for i in range(0, 5):
    print(str(i) * 5)
"""
00000
11111
22222
33333
44444
"""

print('----------')

for i in range(1, 6):
    print(i, i, i, i, i)    # im prinzip das gleiche wie oben, außer das komma getrennt wird
"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
"""

print('----------')

for i in range(1, 5):
    print(str(i) * 5)
"""
11111
22222
33333
44444
"""
