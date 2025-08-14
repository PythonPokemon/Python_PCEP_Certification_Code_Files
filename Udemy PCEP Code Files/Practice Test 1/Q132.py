"""
x ist eine dreidimensionale Liste (Liste von Listen von Listen).
Es besteht aus 2 Hauptelementen (zwei Listen), die jeweils wieder 2 Listen mit Zahlen enthalten.
Visualisierung:

Index	Inhalt
x[0]	[[1, 2], [3, 4]]
x[1]	[[5, 6], [7, 8]]
------------------------------------------------------------------------------------------------
Warum taucht x nicht in der Funktion func auf?
1. Unterschied: Variable vs. Parameter
x ist eine Variable, die eine komplexe Liste speichert (dreidimensional).

Die Funktion func arbeitet mit dem Parameter data, also einem beliebigen Wert, der ihr beim Aufruf übergeben wird.

2. Wie wird x benutzt?
Im Code siehst du:

print(func(x[0]))
Hier wird x[0] als Argument an die Funktion func übergeben.
Das bedeutet: data in func ist genau das, was x[0] enthält, nämlich [[1, 2], [3, 4]].

3. Zusammenfassung
Die Funktion kennt nur ihren Parameter data.
Die Variable x wird außerhalb der Funktion benutzt und Teile davon als Argumente übergeben.
Deshalb taucht x in der Funktion nicht direkt auf, sondern nur das, was du ihr übergibst.

Beispiel zur Verdeutlichung:

x = [[[1,2],[3,4]], [[5,6],[7,8]]]

# Übergib x[0] an func:
func(x[0])  # data = x[0] = [[1, 2], [3, 4]]

Die Funktion weiß nichts von x, sie sieht nur data.
"""
x = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
x = [
        [
            [1, 2], [3, 4]
        ],
        [
            [5, 6], [7, 8]
        ]
    ]

def func(data):
    print('data:', data)    # [[1, 2], [3, 4]]
    res = data[0][0]
    print('res:', res)      # 1

    for da in data:         # Schleife über die Unterlisten in data (z.B. [1,2] und [3,4])
        print('da:', da)    # [1, 2] -> [3, 4]
        for d in da:        # Schleife über die Zahlen in der Unterliste
            print('d:', d)  # 1 -> 2 -> 3 -> 4
            if res < d:
                res = d     # Wenn d größer als res ist, setze res auf d
    return res              # Gib das größte gefundene Element zurück

print(x[0])                    # [[1, 2], [3, 4]]

# funktion die auf das mehrdimensionale array zufreift ab hier!
print(func(x[0]))              # 4
print(func([[1, 7], [3, 4]]))  # 7
