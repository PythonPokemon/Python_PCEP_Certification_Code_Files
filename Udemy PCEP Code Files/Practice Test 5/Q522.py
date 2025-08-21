"""
----------------------------------------------------------------------------------------------------------
| Feature           | Erklärung                                                                          |
| ----------------- | ---------------------------------------------------------------------------------- |
| `yield`           | liefert **einen Wert pro Schleifendurchlauf**, merkt sich den Zustand der Funktion |
| Generator         | **speicherfreundlich**, Werte werden nur bei Bedarf erzeugt                        |
| `for x in func()` | iteriert durch die vom Generator erzeugten Werte                                   |
| `list(func())`    | erzeugt eine **vollständige Liste** aller Werte                                    |
----------------------------------------------------------------------------------------------------------
💡 Merksatz:

yield ≠ return → return beendet die Funktion, yield „pausiert“ sie und liefert Werte nacheinander
Gut für große Datenmengen, weil nicht alles im Speicher gehalten wird
----------------------------------------------------------------------------------------------------------
for i in range(n) → erzeugt i = 0, 1, 2

Du benutzt i aber nicht innerhalb der Schleife → nur s += '*' zählt
Viele Editoren/IDEs (z. B. PyCharm, VS Code) grauen ungenutzte Variablen aus, um dir zu zeigen: 
„Hey, du brauchst diese Variable nicht wirklich“
----------------------------------------------------------------------------------------------------------
💡 Merksatz:

Ausgegraut = ungenutzt
Verwende _, wenn du die Schleifenvariable nicht brauchst → sauberer Code
----------------------------------------------------------------------------------------------------------
"""
def func(n):
    s = ''              # → leere Zeichenkette zum Start
    for i in range(n):  # → Schleife von 0 bis n-1 | i wird nicht genutzt, saubere konvention wäre statt i ein _ zu benutzen
        s += '*'        # → fügt jedes Mal ein * hinzu
        yield s         # → erzeugt ein Generator-Objekt, das nacheinander Werte liefert, 
                        # ohne die ganze Liste im Speicher zu speichern


for x in func(3):       # → Generator liefert nacheinander:
#       '*'
#       '**'
#       '***'
    print(x, end='')    # → alles wird hintereinander gedruckt → ****** | kein Zeilenumbruch da end=''

print()
print(func(3))          # Das ist noch keine Liste, deshalb wird <generator object ...> angezeigt
print(list(func(3)))    # list(generator) → erzeugt alle Werte auf einmal als Liste ['*', '**', '***']
