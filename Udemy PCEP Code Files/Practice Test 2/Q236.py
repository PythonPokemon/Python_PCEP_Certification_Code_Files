"""
in deinem Fall wandert der Lese-Index i von 1 bis 5,
und bei jedem Schritt kopierst du den Wert rechts (data[i]) eine Position nach links (data[i - 1]).
i == ist der schleifen durchlauf!
--------------------------------------------------------------------------------------------------------
| ----------- | --------------- | ------------------------------- | ------------------- |
| Schritt (i) | Liest `data[i]` | Schreibt nach `data[i-1]`       | Liste danach        |
| ----------- | --------------- | ------------------------------- | ------------------- |
| 1           | 2               | auf Index Position 0            |  [2, 2, 3, 4, 5, 6] |
| 2           | 3               | auf Index Position 1            |  [2, 3, 3, 4, 5, 6] |
| 3           | 4               | auf Index Position 2            |  [2, 3, 4, 4, 5, 6] |
| 4           | 5               | auf Index Position 3            |  [2, 3, 4, 5, 5, 6] |
| 5           | 6               | auf Index Position 4            |  [2, 3, 4, 5, 6, 6] |
| ----------- | --------------- | ------------------------------- | ------------------- |
--------------------------------------------------------------------------------------------------------

"""

#Index  0  1  2  3  4  5
data = [1, 2, 3, 4, 5, 6]

for i in range(1, 6):  # 1 -> 2 -> 3 -> 4 -> 5
    data[i - 1] = data[i]   # → das Element links wird durch das nächste Element rechts ersetzt.
                            # Man schiebt also im Prinzip alle Elemente nach links, überschreibt das vorherige Element.

print(data)  # [2, 3, 4, 5, 6, 6]

# This is just for output:
# for i in range(0, 6):
#     print(data[i], end=' ')  # 2 3 4 5 6 6
