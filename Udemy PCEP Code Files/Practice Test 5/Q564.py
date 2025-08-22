"""
--------------------------------------------------------------------------

--------------------------------------------------------------------------
💡 Merksatz

assert → Sicherheitsprüfung, wird nur ausgeführt, wenn Bedingung False ist
Nützlich, um fehlerhafte Eingaben früh abzufangen
remove_min verändert die Liste direkt und gibt sie zurück
--------------------------------------------------------------------------
"""

def remove_min(s):
    assert type(s) == list  # Überprüft: s muss vom Typ Liste sein | Wenn nicht → AssertionError
    assert len(s) > 0       # Überprüft: die Liste ist nicht leer  | Wenn leer → AssertionError
    m = min(s)              # Findet das kleinste Element in der Liste s
    s.remove(m)             # Entfernt das erste Vorkommen von m aus der Liste
    return s                # Gibt die veränderte Liste zurück

print(remove_min([1, 2, 3]))  # [2, 3]
# print(remove_min('Hello'))  # ... AssertionError
# print(remove_min([]))       # ... AssertionError

"""
Liste: [1, 2, 3]
Kleinste Zahl: 1
Nach remove → [2, 3] ✅
"""