"""
rekursive Funktionen
------------------------------------------------------------------------------------------------------
2️⃣ Aufruf

print(func(0, 3))
Start: x = 0, y = 3

Ablauf:
func(0, 3) → 0 == 3? Nein → return func(0, 2)
func(0, 2) → 0 == 2? Nein → return func(0, 1)
func(0, 1) → 0 == 1? Nein → return func(0, 0)
func(0, 0) → 0 == 0? Ja → return 0

Dann wird die 0 zurück durch alle Funktionsaufrufe propagiert

Ergebnis: 0
------------------------------------------------------------------------------------------------------
Wichtig zu verstehen
Rekursion arbeitet rückwärts: Die Funktion ruft sich selbst auf, bis die Abbruchbedingung erfüllt ist.
Abbruchbedingung ist entscheidend, sonst würde die Funktion unendlich laufen.
Alles, was nach return func(...) kommt (z.B. return y + func(...)) wird nicht mehr ausgeführt, 
weil return die Funktion sofort verlässt.
------------------------------------------------------------------------------------------------------
💡 Mini-Erklärung für Teilnehmer
Die Funktion prüft, ob x gleich y ist. 
Wenn nicht, ruft sie sich selbst mit y-1 auf, bis y = x ist. 
Dann gibt sie diesen Wert zurück. Man kann sich das vorstellen wie ein Countdown von y bis x.“
------------------------------------------------------------------------------------------------------
"""

def func(x, y):
    if x == y:
        return x
    else:
        return func(x, y-1) # hier ist der knackpunkt! y-1 sagt unten bei den argumenten 3 das für y steht== runterzählen
        

print(func(0, 3))           # ruft sich immer wider erneut auf, solange y nicht x entspricht! == 0

