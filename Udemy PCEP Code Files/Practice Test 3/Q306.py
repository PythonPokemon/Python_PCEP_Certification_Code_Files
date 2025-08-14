"""
Kurzfassung
data enthält verschiedene Datentypen: Zahl, Dictionary, Tuple, leeres Tuple, Set, Liste.
Eine Schleife prüft den Typ jedes Elements und gibt dafür Punkte:

list → +1
tuple → +10
set → +100
dict → +1000
alles andere → +10000

Am Ende ergibt die Summe 11121.
--------------------------------------------------------------------------------------------

Ausführliche Erklärung
1. Liste mit verschiedenen Datentypen

data = [1, {}, (2,), (), {3}, [4, 5]]

Enthält:
1 → int
{} → dict (leeres Wörterbuch)
(2,) → tuple (ein Element, Komma ist wichtig)
() → tuple (leer)
{3} → set (Menge)
[4, 5] → list (Liste)
--------------------------------------------------------------------------------------------

Auswertung Schritt für Schritt:
| --------- | -------- | ----- | ------ | ------------- |
| Index `i` | Element  | Typ   | Punkte | Zwischensumme |
| --------- | -------- | ----- | ------ | ------------- |
| 0         | `1`      | int   | 10000  | 10000         |
| 1         | `{}`     | dict  | 1000   | 11000         |
| 2         | `(2,)`   | tuple | 10     | 11010         |
| 3         | `()`     | tuple | 10     | 11020         |
| 4         | `{3}`    | set   | 100    | 11120         |
| 5         | `[4, 5]` | list  | 1      | 11121         |
| --------- | -------- | ----- | ------ | ------------- |
"""


data = [1, {}, (2,), (), {3}, [4, 5]]   # länge 6
points = 0

for i in range(len(data)):
    if type(data[i]) == list:
        points += 1
    elif type(data[i]) == tuple:
        points += 10
    elif type(data[i]) == set:      # wenn man in einem dictionary wert setzt!
        points += 100
    elif type(data[i]) == dict:
        points += 1000
    else:
        points += 10000

print(points)  # 11121

data = [1, {}, (2,), (), {3}, [4, 5]]
for i in range(len(data)):
    print(type(data[i]))


"""
i geht also durch die liste von data und prüft jeden einzelen index von links angefanfen, welchem daten typ es entspricht in der if,else abfrgae
und vergiebt dementsprechend punkte und so in jeder weiteren schleife bis alle indizes durchlaufen sind, dann werde die punkte ausgegebn.
und die datentypen ausgegeben, das sich auf den Indizes befindet bsp. 1 'class' int usw.
"""