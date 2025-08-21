"""
data.copy() erzeugt eine flache Kopie des Dictionaries
person ist ein neues Objekt im Speicher, auch wenn die Inhalte gleich sind
--------------------------------------------------------------------------
id() gibt die Speicheradresse eines Objekts zurück
Verschiedene Objekte → unterschiedliche IDs → False
--------------------------------------------------------------------------
"""

data = {'name': 'Peter', 'age': 30} # ein Dictionary mit zwei Einträgen
person = data.copy()
print(id(data) == id(person))  # False, da unterschiedliche referenzen

print(id(data))     # 2513617019072
print(id(person))   # 2513617430784
print()

# ohne flache kopie sind die adressen identisch
person = data
print(id(data) == id(person))  # True

# test
print(id(data))     # 2513617019072
print(id(person))   # 2513617019072