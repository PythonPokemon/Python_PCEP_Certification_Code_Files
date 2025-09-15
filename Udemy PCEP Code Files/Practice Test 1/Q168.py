"""
Frage 97
Übersprungen
Q168

What happens when the user runs the following code?
--------------------------------------------------------
Richtige Antwort
The code outputs 3
--------------------------------------------------------
Ablauf Schritt für Schritt:

i=0: 2*0 < 4 → True → total = 1
i=1: 2*1 < 4 → True → total = 2
i=2: 2*2 < 4 → False → keine Änderung (total = 2)
i=3: 2*3 < 4 → False → keine Änderung (total = 2)

Schleife fertig → else-Block wird ausgeführt → total = 3
--------------------------------------------------------
"""

total = 0                     # Startwert von total = 0
for i in range(4):            # i läuft durch 0,1,2,3  (4 ist exklusiv)
    if 2 * i < 4:             # Bedingung prüfen
        total += 1            # wenn Bedingung wahr ist -> total +1
else:                         # else gehört zur for-Schleife (nicht zum if!)
    total += 1                # wird einmal am Ende der Schleife ausgeführt

print(total)                  # 3
