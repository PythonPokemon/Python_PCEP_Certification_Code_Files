"""
List Comprehension [0 for i in range(1, 3)]

Das ist eine Listen-Komprehension.
Für jedes Element i im Bereich range(1, 3) wird der Wert 0 in die Liste eingefügt.
Da range(1, 3) zwei Werte hat (1 und 2), wird auch zweimal die 0 hinzugefügt.
Das ergibt also:

[0, 0]
"""
# 'mit' List Comprehension:
my_list = [0 for i in range(1, 3)]  # Da range(1, 3) zwei Werte hat (1 und 2), wird auch zweimal die 0 hinzugefügt.
print(my_list)                      # [0, 0]
print(len(my_list))                 # 2 | Da wir zwei Elemente (0, 0) haben, ist die Länge 2.
print('-----')

# 'ohne' List Comprehension:
my_list2 = []           # erzeugt eine leere Liste
for i in range(1, 3):   # erzeugt 2 elemente default [0, 0], da start index:1 bis 2 ist, da 3 ausgeschlossen (exclusiv)
    my_list2.append(1)  # weist allen elementen in der liste denselben wert zu, von [0, 0] auf [1, 1]
print(my_list2)         # [1, 1]
print(len(my_list2))    # 2
