"""
Achtung die Funktion .sorted()
sortiert nach dem key, nicht nach dem enthaltenen wert im key!

also key:   x,  y,  z
            |   |   |
            7   42  23

.
"""
data = {'z': 23, 'x': 7, 'y': 42}

for _ in sorted(data):
    print(data[_], end=' ')  # gibt die in den key's gespeicherten werte, sortiert und end=' ' horizontal hintereinander aus: 7 42 23 

print()
print(sorted(data))          # gibt die key's aus, aber in sortierter reihenfolge ['x', 'y', 'z']
print(data)                  # {'z': 23, 'x': 7, 'y': 42}

for _ in ['x', 'y', 'z']:
    print(data[_], end=' ')  # 7 42 23

