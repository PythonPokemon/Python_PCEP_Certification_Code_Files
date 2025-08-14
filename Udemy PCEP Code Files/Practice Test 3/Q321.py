"""
Kurzfassung
Ein Dictionary speichert Schlüssel-Wert-Paare.
data['x', 'y'] funktioniert nur, wenn der Schlüssel genau dieses Tupel ist.
Einzelne Schlüssel müssen getrennt abgefragt werden: data['x'], data['y'].
Man kann Tupel als Schlüssel verwenden: data = {('x', 'y'): 1} → dann funktioniert data['x', 'y'].
------------------------------------------------------------------------------------------------------------------------------

Schlüssel: 'x',     'y',    'z'
            |        |       |
Werte:      1,       2,      3

------------------------------------------------------------------------------------------------------------------------------
Mini-Erklärung 
„Ein Dictionary speichert Paare aus Schlüssel und Wert. 
Wenn du mehrere Schlüssel zusammen abfragst, müssen sie entweder einzeln existieren oder du erstellst ein Tupel als Schlüssel. 
Sonst gibt Python einen KeyError.“
"""


data = {'x': 1, 'y': 2, 'z': 3} # Tupel {'schlüssel':dazugehörigerWert}
print(data['x', 'y'])           # Python sucht genau den Schlüssel ('x', 'y') → existiert nicht → KeyError: | kommentiere es aus zum testen!

print(data['x'], data['y'], data['z'])     # Einzelne Schlüssel können getrennt abgefragt werden ✅ 1 2 3

data = {('x', 'y'): 1}          # Der Schlüssel ist jetzt das Tupel ('x', 'y') deren zuweisung 1
print(data['x', 'y'])           # ✅ 1
