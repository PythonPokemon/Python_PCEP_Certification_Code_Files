"""
Erklärung:
1. Dictionaries in Python

Ein Dictionary (dict) speichert Schlüssel/Wert-Paare.
Wichtig: Schlüssel müssen eindeutig sein.
Wenn du denselben Schlüssel mehrfach einfügst, überschreibt der letzte Wert den vorherigen.
-------------------------------------------------------------------------------------------

1 (int) und 1.0 (float) sind für Python derselbe Schlüssel in einem Dictionary!
👉 Grund: 1 == 1.0 ist True und beide haben denselben Hashwert.

Daher überschreibt data[1.0] = 4 den Eintrag data[1] = 1.
Der Schlüssel '1' (String) ist aber ein anderer Typ, also bleibt der Eintrag separat.
-------------------------------------------------------------------------------------------
Die Schleife

res = 0
for d in data:
    res += data[d]

data hat die Keys 1 und '1'.
data[1]     = 4, 
data['1']   = 2.

Also: res = 0 + 4 + 2 = 6.

"""
data = {}       # erzeugung dictionary
data[1] = 1     # key 1: wert 1
data['1'] = 2   # auch aber separater, key '1' wert 2
data[1.0] = 4   # key 1 obwohl float überschreibt den wert 1 auf 4 | weil egal ob ein int 1 oder float 1 | 1 key == 1.0 key

res = 0
for d in data:
    res += data[d]               # d geht durch data und speichert die werte in d und d wiederum in res |

print(res)                       # res = 0 + 4 + 2 = 6

print(data)                      # {1: 4, '1': 2}
print({1: 7, 1.0: 23, 1.1: 42})  # {1: 23, 1.1: 42} | der vorherige 1: 7, wird durch 1.0: 23, ersetzt
