"""
✅ Merksatz

None = „kein Wert / leer“
Kann Variablen zugewiesen werden
Kann verglichen werden (is None)
Nicht für Rechnungen verwenden
Universell einsetzbar, nicht nur in Funktionen
"""

"""
Erklärung:
None ist ein spezieller Wert in Python, der „kein Wert“ oder „leer“ bedeutet
Du kannst ihn einer Variablen zuweisen, wenn die Variable noch keinen echten Wert hat
"""
# Der Wert None kann Variablen zugewiesen werden.:
x = None
print(x)  # None
#-----------------------------------------------------------------------------------------------------------
"""
Erklärung:

Mit is prüft man, ob eine Variable genau None ist
Hier ist y = 3, also y is None → False
"""
# Der Wert None kann mit Variablen verglichen werden.:
y = 3
print(y is None)  # False
#-----------------------------------------------------------------------------------------------------------
"""
print(None + 7)  # TypeError: unsupported operand ...

Erklärung:
None ist kein Zahlenwert
Addition, Subtraktion oder andere arithmetische Operationen funktionieren nicht → Python wirft einen Fehler
Der Wert None kann nicht als Argument für arithmetische Operatoren verwendet werden.
"""
#-----------------------------------------------------------------------------------------------------------
"""
Erklärung:
None kann überall in Python verwendet werden, nicht nur in Funktionen
"""
# Der Wert None kann auch außerhalb von Funktionen verwendet werden:
z = None
print(z)  # None
