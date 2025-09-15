"""
Ablauf im Detail:
-----------------------------------------------------------
| z (aus x) | z in y? | Aktion        | res nach Addition |
| --------- | ------- | ------------- | ----------------- |
| 1         | nein    | addiere 1     | 1 + 1 = 2         | 
| 4         | ja      | skip/continue | 2                 |
| 7         | nein    | addiere 7     | 2 + 7 = 9         |
| 9         | nein    | addiere 9     | 9 + 9 = 18        |
| 10        | ja      | skip/continue | 18                |
| 11        | nein    | addiere 11    | 18 + 11 = 29      |
-----------------------------------------------------------
immer wenn nein, wird die zahl ausgegeben, 
und dem res wert dazu addiert, also: 
1 -> 7 -> 9 -> 11
"""


x = (1, 4, 7, 9, 10, 11)
y = {2: 'A', 4: 'B', 6: 'C', 8: 'D', 10: 'E', 12: 'F'}
res = 1

for z in x:         # z iteriert durch x
    if z in y:      # Prüft: ist z ein Schlüssel im Dictionary y?
        continue    # # Wenn ja, überspringe den Rest der Schleife
    else:
        print('z:', z)  # 1 -> 7 -> 9 -> 11
        res += z        # summiert nur Werte aus x, die nicht als Schlüssel in y existieren

print(res)  # 29       == 1 + 7 + 9 + 11
