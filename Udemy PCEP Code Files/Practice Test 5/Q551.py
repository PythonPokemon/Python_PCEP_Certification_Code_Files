"""
2️⃣ Indexing
print(my_tuple[2])  # 3


[2] → greift genau auf das Element mit Index 2 zu

Index 2 = 3 ✅
--------------------------------------------------------------------------------------------------------------------
3️⃣ Slicing
print(my_tuple[1:3])  # (2, 3)


[start:end] → Start inklusiv, End exklusiv
Start = 1 → Element 2
End = 3 → bis, aber nicht einschließlich Index 3 → Elemente 1,2 werden ignoriert, Index 3 = 4 wird nicht mitgenommen
Ergebnis = (2, 3) ✅
--------------------------------------------------------------------------------------------------------------------
Merksatz

Indexing fängt man bei 0 an

Slicing fängt man auch bei 0 an vom startpunkt
aber wenn man den Endpunkt zählt, fängt man bei 1 an

[start:end] → von start inklusive bis end exklusive
Deshalb [1:3] = (2, 3) und nicht (2, 4)
--------------------------------------------------------------------------------------------------------------------
"""
my_tuple = (1, 2, 3, 4)
# Indexing:
print(my_tuple[2])  # 3
# Slicing:
print(my_tuple[1:3])  # (2, 3)

# They CANNOT be modified using the del instruction:
# del my_tuple[0]
# TypeError: 'tuple' object doesn't support item deletion

# They CANNOT be extended using the .append() method:
# my_tuple.append(5)
# AttributeError: 'tuple' object has no attribute 'append'
