"""
Wenn minus 2 dem wert 3 entspricht inklusive und exklusive -1 den wert 4 
dann bleibt der wert 3 der ausgegebn wird
------------------------------------------------------------------------
weil bei minus zählung man von rechts beginnt!
"""

data = (1, 2, 3, 4)
data = data[-2:-1]  # weiß data die eine tupel beinhalte
print(data)  # (3,)
data = data[-1]
print(data)  # 3
