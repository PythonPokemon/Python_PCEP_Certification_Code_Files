"""
Kurz beschreibung

C bekommt den startwert 0 zugewiesen
dann folgt eine schleife, diese wird solange C kleiner 5 ist durchegführt 
C bekommt bei jedem erneuten durchlauf zu dem aktuellem wert + 1 dazu addiert
wenn C den wert 3 entspricht, wird übersprungen.
Ausgabe C, ohne Zeilenumbruch und Leerzeichen
"""
c = 0
while c < 5:
    c = c + 1
    if c == 3:
        continue
    print(c, end="")  # 1245
