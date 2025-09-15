"""
Frage 62
Übersprungen
Q550

What is the output of the following snippet?

tup = (1, ) + (1, )
tup = tup + tup
print(len(tup))
--------------------------------------------
Richtige Antwort
4
"""


tup = (1, ) + (1, ) # (1, ) + (1, ) == (1, 1)
print(tup)          # (1, 1)

tup = tup + tup     # (1, 1) +  (1, 1) == (1, 1, 1, 1)
print(tup)          # (1, 1, 1, 1)

print(len(tup))  # 4

"""
Index:               0  1  2  3 
Elemente:            |  |  |  |  == 4
                    (1, 1, 1, 1)
"""