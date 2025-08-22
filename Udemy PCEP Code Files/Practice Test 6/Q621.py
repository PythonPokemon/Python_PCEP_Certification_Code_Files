"""
Die innere funktionsvariable greift auf die globale variable zu, 
die bereits x den wert 1 zugewiesen hat
-----------------------------------------------------------------------
Merksatz für Anfänger

Nur lesen → keine lokale Zuweisung → greift auf globale Variable zu
Mit Zuweisung (= oder +=) ohne global → Python erstellt lokale Variable
global x → erlaubt, die globale Variable zu ändern
-----------------------------------------------------------------------
Visualisierung

Global: x = 1

func():
    kein lokales x
    benutzt global x
    berechnet x + 1 ist 2
    Ausgabe -> 2

Nach func(): global x bleibt 1
-----------------------------------------------------------------------
"""

def func():
    print(x + 1, end=' ')  # greift auf globale x zu

x = 1
func()   # 2
print(x) # 1
