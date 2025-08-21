"""
data ist eine Liste mit 6 Elementen
Manche Elemente sind Zahlen (int)
Manche Elemente sind verschachtelte Listen (list)
-------------------------------------------------
| i | data\[i] | type(data\[i]) |  Liste?  |
| - | -------- | -------------- |  ------  |
| 0 | 1        | int            | ❌      |
| 1 | 2        | int            | ❌      |
| 2 | \[3, 4]  | list           | ✅      |
| 3 | \[5, 6]  | list           | ✅      |
| 4 | 7        | int            | ❌      |
| 5 | \[8, 9]  | list           | ✅      |
-------------------------------------------------
"""

# typ   int    list    list  int  list
#Index  0  1     2       3    4     5
data = [1, 2, [3, 4], [5, 6], 7, [8, 9]]
count = 0

for i in range(len(data)):          # range(len(data)) → erzeugt 0, 1, 2, 3, 4, 5
    if type(data[i]) == list:       # data[i] → greift auf jedes Element der Liste zu und prüft ob elemente dem typ einer liste entsprechen
        count += 1                  # Wenn ja ,type(data[i]) == list → count += 1 

print(count)                        # Es gibt 3 Unterlisten: [3,4], [5,6], [8,9] | Deshalb Ausgabe: 3 ✅
