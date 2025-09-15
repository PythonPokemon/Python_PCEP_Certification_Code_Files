"""
Frage 61
Übersprungen
Frage 340

An alternative name for a data structure called a stack is: | Ein alternativer Name für eine Datenstruktur, die als Stack bezeichnet wird, lautet:
--------------------------------------------------------------------------------------------------------------------------------------------------
Richtige Antwort
LIFO

Erklärung
LIFO steht für Last In, First Out, was ein grundlegendes Merkmal einer Stack-Datenstruktur ist. 
In einem Stack ist das zuletzt hinzugefügte Element das erste, das entfernt wird, was LIFO zu einem alternativen Namen für einen Stack macht.
--------------------------------------------------------------------------------------------------------------------------------------------------
"""

x = []          # []
x.append(1)     # [1]
x.append(2)     # [1, 2]
x.append(3)     # [1, 2, 3]
print(x)        # [1, 2, 3]
print(x.pop())  # nimmt jeweils das element raus das zuletzt hinzugefügt wurde == 3
print(x.pop())  # nimmt jeweils das element raus das zuletzt hinzugefügt wurde == 2
print(x.pop())  # nimmt jeweils das element raus das zuletzt hinzugefügt wurde == 1
print(x)        # []