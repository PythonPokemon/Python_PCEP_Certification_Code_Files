"""
Frage 75
Übersprungen
Q152

What is the output of the following snippet?
----------------------------------------------------------------------------------------------------------------
Richtige Antwort
two
----------------------------------------------------------------------------------------------------------------
| Schlüssel | Wert      |
| --------- | --------- |
| `'one'`   | `'two'`   |
| `'three'` | `'one'`   |
| `'two'`   | `'three'` |

2.Was macht v = dictionary['one']?
Du holst den Wert zum Schlüssel 'one' aus dem Dictionary.
dictionary['one'] ist 'two' (laut oben).
Also wird v zunächst auf 'two' gesetzt.

3. Schleife for k in range(3):
range(3) erzeugt die Zahlen 0, 1, 2 → drei Schleifendurchläufe.

print(v)
v = dictionary[v]
Du gibst den aktuellen Wert von v aus und aktualisierst v mit dem Wert, der im Dictionary zum Schlüssel v steht.
----------------------------------------------------------------------------------------------------------------
4. Schritt-für-Schritt Ablauf:
| Schleifendurchlauf | `v` vor print | Ausgabe `print(v)` | `v = dictionary[v]`          |
| ------------------ | ------------- | ------------------ | ---------------------------- |
| 1 (k=0)            | `'two'`       | two                | dictionary\['two'] = 'three' |
| 2 (k=1)            | `'three'`     | three              | dictionary\['three'] = 'one' |
| 3 (k=2)            | `'one'`       | one                | dictionary\['one'] = 'two'   |
----------------------------------------------------------------------------------------------------------------
"""

dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}  
# Dictionary mit Schlüssel-Wert-Paaren: 'one'→'two', 'three'→'one', 'two'→'three'

v = dictionary['one']  
# Hole den Wert zum Schlüssel 'one' → 'two'  
# Setze die Variable v auf 'two'

# for k in range(len(dictionary)):  # Alternative: Schleife über Anzahl der Elemente im Dictionary
for k in range(3):  
    # Schleife läuft 3-mal (k = 0, 1, 2)
    
    print(v)  
    # Ausgabe der aktuellen Variable v
    # Im ersten Durchlauf: 'two'
    # Im zweiten Durchlauf: 'three'
    # Im dritten Durchlauf: 'one'
    
    v = dictionary[v]  
    # Aktualisiere v auf den Wert im Dictionary zum aktuellen Schlüssel v
    # z.B. dictionary['two'] → 'three' im ersten Durchlauf
    # dictionary['three'] → 'one' im zweiten Durchlauf
    # dictionary['one'] → 'two' im dritten Durchlauf

print(v)  
# Ausgabe des finalen Wertes von v nach der Schleife
# Ergebnis: 'two'

