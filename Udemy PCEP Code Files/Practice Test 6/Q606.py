"""
💡 Merksatz:

Du druckst immer zuerst den aktuellen Wert,
dann springst du im Dictionary auf den Wert, der dazu gehört.
So entsteht ein Hin-und-her-Zyklus zwischen 0 und 1.
"""
#KV == Key Value
#KV       1     2     3     4
data = {1: 0, 2: 1, 3: 2, 0: 1} # (len(data)) == länge 4
x = 0

for _ in range(len(data)):  # Schleife, die eine bestimmte Anzahl von Malen läuft | indem fall 4
    print(x)                # 0 - 1 - 0 - 1
    x = data[x]             # x zeigt auf einen Schlüssel | 
                            # data[x] sagt dir: „Springe zu dem Wert, der hinter diesem Schlüssel steht“
                            # Dann speicherst du das wieder in x → nächster Sprung
print(x)      # 0
