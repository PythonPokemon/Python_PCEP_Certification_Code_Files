"""
Mini-Erklärung

In Python können mehrere Variablen auf dieselbe Liste zeigen. 
Änderungen über eine Variable wirken auf alle Referenzen. 
Mit [:] kann man eine echte Kopie erstellen, die unabhängig ist. 
So erklären sich die unterschiedlichen Effekte beim Zählen in der Schleife.“
"""


fruits1 = ['Apple', 'Pear', 'Banana']

fruits2 = fruits1       # fruits2 zeigt auf die gleiche Liste wie fruits1
fruits3 = fruits1[:]    # fruits3 ist eine **neue Kopie** von fruits1

fruits2[0] = 'Cherry'
fruits3[1] = 'Orange'

res = 0

for i in (fruits1, fruits2, fruits3):
    if i[0] == 'Cherry':
        res += 1
    if i[1] == 'Orange':
        res += 10

print(res)          # 12

# gibt die speicheradresse aus!
print(id(fruits1))  # e.g. 140539383900864
print(id(fruits2))  # e.g. 140539383900864 (the same number)
print(id(fruits3))  # e.g. 140539652049216 (a different number)
print()

# Prüfe den index der listen, nach änderung!!
# liste1
print("Liste1: ",fruits1)
print(fruits1[0])
print(fruits1[1])
print(fruits1[2])
print()

# liste2
print("Liste2: ",fruits2)
print(fruits2[0])
print(fruits2[1])
print(fruits2[2])
print()

# liste3
print("Liste3: ",fruits3)
print(fruits3[0])
print(fruits3[1])
print(fruits3[2])
print()