"""
📌 Ist das ungewöhnlich?

Nein 😊 - es ist nur eine Kurzschreibweise.
Man kann Ausdrücke direkt in Funktionsaufrufe schreiben, z. B.:

print(len("Hallo"))       # direkt String übergeben
print(sum([10, 20, 30]))  # direkt Liste übergeben
print(max(range(1, 5)))   # direkt range übergeben

📌 print(remove_min([1, 2, 3])) 📌
--------------------------------------------------------------------------
🎯 Fazit

✅ s ist eine Liste, wenn man sie als Liste übergibt (wie [1, 2, 3]).
✅ Der assert stellt sicher, dass es auch wirklich eine Liste ist.
✅ Der assert len(s) > 0 stellt sicher, dass sie nicht leer ist.
✅ s.remove(...) verändert die Liste direkt und gibt nichts zurück.
✅ Am Ende wird die veränderte Liste zurückgegeben.
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

print(remove_min([1, 2, 3]))  # [2, 3] | hier wird die Liste direkt in der funktion inklusive parameter erzeugt und übergeben
# print(remove_min('Hello'))  # ... AssertionError
# print(remove_min([]))       # ... AssertionError

"""
Liste: [1, 2, 3]
Kleinste Zahl: 1
Nach remove → [2, 3] ✅
"""