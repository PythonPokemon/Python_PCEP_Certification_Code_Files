"""
-----------------------------------------------------------------------------------------------------------
1️⃣ Grundregel
-----------------------------------------------------------------------------------------------------------
Die Funktion len() fragt immer das Objekt, das du ihr übergibst, nach seiner Länge:

String: Länge = Anzahl der Zeichen

s = "Peter"
print(len(s))  # 5
-----------------------------------------------------------------------------------------------------------
Liste / Tuple / Dictionary: Länge = Anzahl der Elemente

data = ['Peter', 'Paul', 'Mary', 'Jane']
print(len(data))  # 4
-----------------------------------------------------------------------------------------------------------
2️⃣ Anwendung in deiner Schleife
-----------------------------------------------------------------------------------------------------------
data = ['Peter', 'Paul', 'Mary', 'Jane']

for d in data:       # d nimmt nacheinander die Werte der Liste an
    if len(d) == 4:  # len() wird auf das aktuelle Element d angewendet
        print(d)


d ist ein String ('Peter', 'Paul', …)
Also: len(d) → Zahl der Zeichen des Strings
Bedingung len(d) == 4 filtert nur Strings mit genau 4 Zeichen → 'Paul', 'Mary', 'Jane'
-----------------------------------------------------------------------------------------------------------
3️⃣ Vergleich mit len(data):
-----------------------------------------------------------------------------------------------------------
for d in data:
    if len(data) == 4:
        print(d)


Hier: len(data) → Länge der Liste (4 Elemente)
Bedingung ist immer True → alle Elemente werden gedruckt
-----------------------------------------------------------------------------------------------------------
4️⃣ Merksatz
-----------------------------------------------------------------------------------------------------------
len() zählt immer die Länge des Objekts, nicht automatisch Zeichen oder Elemente.
Was gezählt wird, hängt vom Typ des Objekts ab:
    String → Zeichen
    Liste  / Tuple → Elemente
    Dict   → Keys
-----------------------------------------------------------------------------------------------------------
| Datentyp       | Beispiel                        | `len()` Ergebnis | Erklärung                         |
| -------------- | ------------------------------- | ---------------- | --------------------------------- |
| **String**     | `s = "Peter"`                   | `len(s) = 5`     | Zählt die **Anzahl der Zeichen**  |
| **Liste**      | `lst = ['Peter','Paul','Mary']` | `len(lst) = 3`   | Zählt die **Anzahl der Elemente** |
| **Tuple**      | `t = (1,2,3,4)`                 | `len(t) = 4`     | Zählt die **Anzahl der Elemente** |
| **Dictionary** | `d = {1:'A',2:'B',3:'C'}`       | `len(d) = 3`     | Zählt die **Anzahl der Keys**     |
| **Set**        | `s = {1,2,3}`                   | `len(s) = 3`     | Zählt die **Anzahl der Elemente** |
-----------------------------------------------------------------------------------------------------------

"""
data = ['Peter', 'Paul', 'Mary', 'Jane']
for d in data:
    if len(d) == 4: # hier sucht die .len() methode nach strings mit 4 zeichen! und gibt diese aus | ACHTUNG! wenn (data) stehen würde, dann wäre es ebenfals richtig, da nur nach 4 elementen in der liste gesucht wird, was ebenfalls 4 entspricht!
        print(d)

"""
Paul
Mary
Jane
"""

print('----------')

data = ['Peter', 'Paul', 'Mary', 'Jane']
da = data[1:]   # ACHTUNG STARTWERT    INDEX 1 in liste 'da' die den gleichen verweis auf die liste von 'data' bekommt
for d in data:  # aber iteriert wird nicht in 'da' sondern durch 'data' und diese liste ist unverändert! 
    print(d)

"""
Peter
Paul
Mary
Jane
"""

print('----------')

data = ['Peter', 'Paul', 'Mary', 'Jane']
for d in data:
    if len(d) != 4: # sucht zeichenketten die un gleich 4 sind
        print(d)

"""
Peter
"""

print('----------')

data = ['Peter', 'Paul', 'Mary', 'Jane']
for d in data:
    print(d)

"""
Peter
Paul
Mary
Jane
"""
