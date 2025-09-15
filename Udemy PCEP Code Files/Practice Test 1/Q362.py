"""
Frage 102
Übersprungen
Q362

Select the true statement:
-------------------------------------------------------------
Richtige Antwort
Keyword arguments cannot be followed by positional arguments. | Schlüsselwortargumente dürfen nicht von Positionsargumenten gefolgt werden.

"""


def my_function(a=23, b=42):    # Funktion mit zwei Parametern und Defaultwerten
    print(a, b)

# my_function(a=11, 17)         # ❌ SyntaxError
                                # Grund: "a=11" ist ein Schlüsselwortargument (keyword argument),
                                #        "17" ist ein Positionsargument (positional argument).
                                
                                # Regel in Python: 
                                # ZUERST Positionsargumente, DANN Schlüsselwortargumente.
                                # Umgekehrt ist nicht erlaubt.

"""
✅ Korrekt wäre zum Beispiel:

my_function(11, 17)             # beide als Positionsargumente -> Ausgabe: 11 17
my_function(a=11, b=17)         # beide als Schlüsselwortargumente -> Ausgabe: 11 17
my_function(11, b=17)           # Mischung erlaubt aber! ZUERST Positionsargumente, DANN Schlüsselwortargumente.-> Ausgabe: 11 17
"""