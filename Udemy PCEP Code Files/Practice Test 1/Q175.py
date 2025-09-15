"""
Frage 95
Übersprungen
Q175

What is the expected result of the following code?
--------------------------------------------------
2
"""

# Index:  0    1    2
rates = (1.2, 1.4, 1.0) # Tupel mit 3 elementen
new = rates[3:]         # erzeugt leeres tupel weil auf index 3 es keinen eintrag gibt, wenn index 0-2 angegeben wäre, würden entsprechend diese werte übergeben werden: (1.2, 1.4, 1.0)
print(new)              # () leer | kein eintrag
print(rates[-2:])       # (1.4, 1.0) | von Index 3 minus 2 inklusive

for rate in rates[-2:]: # rate iteriert rückwärts durch rates, startpunkt inklusive -2 und speichert die werte in sich
    new += (rate,)      # die werte in rate werden new zugewiesen

print(new)              # (1.4, 1.0)
print(len(new))         # 2
