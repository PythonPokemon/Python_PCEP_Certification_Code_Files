"""
Kurzfassung

nums[::-1] kehrt die Liste um.
[0] nimmt das erste Element der umgedrehten Liste (also das letzte ursprüngliche Element).
len(nums) - nums[::-1][0] berechnet die Differenz zwischen der Länge der Liste und dem letzten Element → hier 3 - 3 = 0.
('Peter',) * 0 ergibt ein leeres Tuple ().

Schritt-für-Schritt Erklärung

1. Ausgangsliste
nums = [1, 2, 3]
Liste mit 3 Elementen.

2. Länge der Liste
len(nums)  # 3
len() zählt die Anzahl der Elemente.

3. Umgedrehte Liste
nums[::-1]  # [3, 2, 1]
[::-1] ist ein Slicing-Trick, um die Liste rückwärts zu lesen.
[0] nimmt das erste Element der umgedrehten Liste → 3

4. Differenz berechnen
len(nums) - nums[::-1][0]  # 3 - 3 = 0

5. Tuple erstellen
data = ('Peter',) * 0  # leeres Tuple
('Peter',) ist ein 1-Element-Tuple.
Multiplikation mit 0 wiederholt das Element 0-mal → ()

Mini-Erklärung für Teilnehmer
„Hier wird zuerst die Liste nums umgedreht und das letzte Element ausgewählt. 
Dann wird die Länge der Liste minus diesem Wert berechnet. 
Ist das Ergebnis 0, ergibt die Multiplikation eines Tuples mit 0 ein leeres Tuple. So entsteht ().“
"""
nums = [1, 2, 3]
data = ('Peter',) * (len(nums) - nums[::-1][0])
print(data)  # ()

print(len(nums) - nums[::-1][0])            # 0
print(len([1, 2, 3]) - [1, 2, 3][::-1][0])  # 0
print(3 - [3, 2, 1][0])                     # 0
print(3 - 3)                                # 0
print(0)                                    # 0

print(('Peter',))        # ('Peter',)
print(type(()))          # <class 'tuple'>
print(type('Peter'))     # <class 'str'>
print(('Peter',) * 0)    # ()
print((1, 2, 3) * 0)     # ()
