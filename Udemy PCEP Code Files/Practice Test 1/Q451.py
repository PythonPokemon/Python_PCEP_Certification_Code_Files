"""
Frage 47
Übersprungen
Q451

What is the output of the following snippet?

l1 = [1, 2, 3]
 
for v in range(len(l1)):
    l1.insert(1, l1[v])
 
print(l1)

--------------------------------------------
Richtige Antwort
[1, 1, 1, 1, 2, 3]
"""


l1 = [1, 2, 3]          # erzeugt liste mit 3 elementen: [1, 2, 3] 

for v in range(3):      # iteriert 3 mal durch die list
    l1.insert(1, l1[v]) # fügt in der liste während der iteration den angegeben wert 1 ein, ab beginn des wertes

# eingefügter wert:           |  |  |
print(l1)               # [1, 1, 1, 1, 2, 3]


