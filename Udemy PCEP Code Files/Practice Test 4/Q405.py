"""
1️⃣ Gleichheit vs. Identität
    == prüft den Inhalt → True, weil beide Tuples 'a', 'b' enthalten
    is prüft ob es dasselbe Objekt im Speicher ist → True in deinem Beispiel
-----------------------------------------------------------------------------------------------------------------------------------
2️⃣ Warum is True?
Tuples sind immutable (unveränderlich)
    Python kann identische unveränderliche Objekte im Speicher zusammenführen (interning)

Strings sind immutable
    Auch Strings wie 'a' und 'b' werden intern als gleiches Objekt wiederverwendet

Tuple-Kombinationen aus diesen Strings werden in manchen Python-Versionen optimiert und auf dasselbe Objekt verwiesen
-----------------------------------------------------------------------------------------------------------------------------------
3️⃣ Was du wissen solltest
Dieses Verhalten passiert nur bei unveränderlichen Objekten wie Tuples oder kleinen Strings
Bei Listen oder veränderlichen Objekten passiert das nicht:


list1 = [1, 2]
list2 = [1, 2]

print(list1 == list2)  # True, da beide den gleichen inhalt haben
print(list1 is list2)  # False, da beides unterschiedliche Objekte sind und deshalb jeder seine eigene speicheradresse hat!

Gleicher Inhalt, aber verschiedene Objekte
-----------------------------------------------------------------------------------------------------------------------------------
💡 Mini-Erklärung für Teilnehmer

„== prüft Inhalt, is prüft Identität. 
Bei unveränderlichen Objekten wie Tuples und kleinen Strings kann Python Speicher sparen, indem es gleiche Objekte wiederverwendet. 
Deshalb kann is manchmal True sein, obwohl du scheinbar zwei Objekte erstellt hast.“
-----------------------------------------------------------------------------------------------------------------------------------
"""

data1 = 'a', 'b'        # Tuple mit zwei Strings
data2 = ('a', 'b')      # Tuple mit den gleichen Strings
print(data1 == data2)   # True
print(data1 is data2)   # True
print(id(data1))        # e.g. 140539383900864
print(id(data2))        # e.g. 140539383900864 (the same number)
print(type(data1))      # <class 'tuple'>
print(type(data2))      # <class 'tuple'>
