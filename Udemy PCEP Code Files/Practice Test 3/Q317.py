"""
Länge eines Tuples abfragen
----------------------------------------------------------------------------------------------
print(data.__len__())  # 0
print(len(data))       # 0

Beide Methoden geben die Anzahl der Elemente zurück.
Hier: 0, weil das Tuple leer ist.
len(data) ist die üblichere, Python-konforme Methode.
__len__() ist die interne Methode, die Python unter der Haube aufruft, wenn man len() benutzt.
----------------------------------------------------------------------------------------------
Mini-Erklärung 
„Ein Tuple ist wie eine Liste, nur dass man die Elemente nicht ändern kann.
----------------------------------------------------------------------------------------------
"""


data = ()
print(data.__len__())  # 0 | vom Konstruktor
print(len(data))       # 0 | vom Tupel

print(type(data))      # <class 'tuple'>
