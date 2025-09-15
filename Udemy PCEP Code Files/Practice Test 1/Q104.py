# es wird nur jeder zweite Wert der Liste ausgegeben
#Index
#|-> 0  1  2  3  4  5  6  7  8
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[::2])  # [1, 3, 5, 7, 9]

# oder der erste wert vor dem doppelpunkt setzt den index startwert
print(a[1::2])  # [2, 4, 6, 8]
