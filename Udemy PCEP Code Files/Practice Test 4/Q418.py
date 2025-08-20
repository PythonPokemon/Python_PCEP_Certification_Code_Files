"""
Thema in Python: Klammern und Operator-Reihenfolge.
--------------------------------------------------------------------------------------
Unterschiedliche Schreibweisen von negativen Zahlen und Potenzen
Variante 1:
(-a) ** 2

Klammern zuerst → -a = -7
Dann Potenz: (-7) ** 2 = 49 ✅
--------------------------------------------------------------------------------------
Variante 2:
-(a) ** 2

Klammern um a selbst → a = 7
Potenz hat höhere Priorität als unäres Minus (-)
Also zuerst a ** 2 = 49
Dann - davor → -(49) = -49 ✅
--------------------------------------------------------------------------------------
Variante 3:
-a ** 2

Gleiche Regel: Potenz zuerst → 7 ** 2 = 49
Dann unäres Minus → -49 ✅
--------------------------------------------------------------------------------------
Variante 4:
-(a ** 2)

Klammern machen explizit, was bei Variante 3 automatisch passiert → -(7 ** 2) = -49 ✅
--------------------------------------------------------------------------------------
Wichtig: Operator-Priorität in Python

** → höchste Priorität
- (unäres Minus) → kommt danach
    Nur durch Klammern kannst du das Vorzeichen vor der Potenzierung ändern.
--------------------------------------------------------------------------------------
💡 Merksatz:
(-a) ** 2 → Zuerst negieren, dann potenzieren → Ergebnis positiv
-a ** 2 oder -(a ** 2) → Zuerst potenzieren, dann negieren → Ergebnis negativ
--------------------------------------------------------------------------------------
"""

# a = eval(input('Enter a number for the equation: '))
a = eval('7')     # Wandelt den String '7' in die Zahl 7 um

print((-a) ** 2)  #  49 | Variante 1:Klammern zuerst negieret → -a = -7,  Dann Potenziert: (-7) ** 2 = 49 
print(-(a) ** 2)  # -49 | Variante 2: Potenz zuerst 7 * 7 == 49, Dann unäres Minus ==-49
print(-a ** 2)    # -49 | Variante 3: Potenz zuerst 7 * 7 == 49, Dann unäres Minus ==-49
print(-(a ** 2))  # -49 | Variante 4: Klammern machen explizit
