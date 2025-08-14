"""
 Regeln für gültige Bezeichner (Namen) in Python.
 ------------------------------------------------------------------------------------------
 1️⃣ Regeln für Funktions- und Variablennamen

Ein Name darf nicht mit einer Zahl beginnen
    z.B. 1function → ❌ ungültig
Er darf Buchstaben (a-z, A-Z), Zahlen (0-9) und Unterstriche (_) enthalten
Keine Leerzeichen oder Sonderzeichen
Keine Python-Schlüsselwörter (def, class, if, for …)
------------------------------------------------------------------------------------------
2️⃣ Beispiele aus deinem Code

def 1function(): pass      # ❌ ungültig, beginnt mit Zahl
def _function1(): pass     # ✅ gültig, beginnt mit Unterstrich
def Function1(): pass      # ✅ gültig, beginnt mit Buchstabe
def Function_1(): pass     # ✅ gültig, Buchstaben + Unterstrich + Zahl
def Func_1_tion(): pass    # ✅ gültig, Mischung aus Buchstaben, Unterstrich, Zahl
------------------------------------------------------------------------------------------
💡 Mini-Erklärung für Teilnehmer

„In Python dürfen Funktionsnamen nicht mit einer Zahl anfangen. 
Alles andere - Buchstaben, Zahlen nach dem ersten Zeichen und Unterstriche - ist erlaubt.“
------------------------------------------------------------------------------------------
"""


#def 1function(): pass  # SyntaxError: kommentiere links aus um zu testen!


def _function1():
    pass


def Function1():
    pass


def Function_1():
    pass


def Func_1_tion():
    pass
