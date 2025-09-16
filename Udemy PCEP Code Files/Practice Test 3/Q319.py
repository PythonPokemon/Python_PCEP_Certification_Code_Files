"""
---------------------------------------------------------------------------------------------------
Mini-Erklärung für Teilnehmer

„Hier wird zuerst die Liste nums umgedreht und das letzte Element ausgewählt. == 3
Dann wird die Länge der Liste minus diesem Wert berechnet. länge 3 - letztes element 3 == 0
Ist das Ergebnis 0, ergibt die Multiplikation eines Tuples mit 0 ein leeres Tuple. So entsteht ().“
---------------------------------------------------------------------------------------------------
"""
nums = [1, 2, 3]        # liste, länge 3
data = ('Peter',) * (len(nums) - nums[::-1][0])
print(data)  # ()

print(len(nums) - nums[::-1][0])            # 0 | 3 - 3
print(len([1, 2, 3]) - [1, 2, 3][::-1][0])  # 0
print(3 - [3, 2, 1][0])                     # 0
print(3 - 3)                                # 0
print(0)                                    # 0

print(('Peter',))        # ('Peter',)
print(type(()))          # <class 'tuple'>
print(type('Peter'))     # <class 'str'>
print(('Peter',) * 0)    # () | string * 0 = '' == empty string == empty tuple == ()
print((1, 2, 3) * 0)     # ()
