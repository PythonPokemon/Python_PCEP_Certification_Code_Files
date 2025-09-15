"""
Frage 22
Übersprungen
Q133

What is the expected output of the following code?

nums = [3, 4, 5, 20, 5, 25, 1, 3]
nums.pop(1)
print(nums)

Richtige Antwort
[3, 5, 20, 5, 25, 1, 3]
--------------------------------------------------------------------------------------------------------------------
.pop() in Python

Bedeutung: Entfernt ein Element aus einer Liste an einer bestimmten Position (Index) und gibt dieses Element zurück.
Standardverhalten: Wenn du keinen Index angibst, entfernt .pop() das letzte Element der Liste.
Mit Index: .pop(index) entfernt das Element an dieser Position (Index beginnt bei 0).

| Methode            | Nach was wird gelöscht?  | Gibt Wert zurück?  | Fehler bei Nichtvorhandensein |
| ------------------ | ------------------------ |------------------- | ----------------------------- |
| `.pop(index)`      | Index                    |       ✅ Ja       |       `IndexError`            |
| `.pop()`           | Letztes Element          |       ✅ Ja       |           -                   |
| `.remove(wert)`    | Erster Treffer des Werts |       ❌ Nein     |       `ValueError`            |
| `del liste[index]` | Index                    |       ❌ Nein     |       `IndexError`            |
| `del liste`        | Ganze Variable           |       ❌ Nein     |           -                   |
--------------------------------------------------------------------------------------------------------------------

"""

# .pop([index])
print("bsp.pop():")
nums = [3, 4, 5, 20, 5, 25, 1, 3]
wert = nums.pop(1)     # Entfernt das Element an Index 1 → das ist die Zahl 4
print(nums)     # [3, 5, 20, 5, 25, 1, 3]
print(wert)     # 4

nums.pop()      # Entfernt das letzte Element der Liste → das ist die Zahl 3
print(nums)     # [3, 5, 20, 5, 25, 1] 

#.remove(wert)
"""
Funktion: Entfernt das erste Vorkommen eines bestimmten Werts (nicht per Index).
Fehler: Wenn der Wert nicht existiert → ValueError.

"""
print("")
print("bsp.remove():")
nums2 = [10, 20, 30, 20]
nums2.remove(20)      # entfernt nur das erste 20
print(nums2)          # [10, 30, 20]


#.del()
"""
Funktion: Löscht Elemente per Index oder ganze Variablen.
Keine Rückgabe: Gibt nichts zurück.
Fehler: Wenn der Index nicht existiert → IndexError.

"""

print("")
print("bsp.del():")
nums3 = [10, 20, 30]
del nums3[1]          # entfernt Element an Index 1 → 20
print(nums3)          # [10, 30]

del nums3             # löscht die gesamte Variable
# print(nums) würde jetzt einen Fehler geben, weil nums nicht mehr existiert