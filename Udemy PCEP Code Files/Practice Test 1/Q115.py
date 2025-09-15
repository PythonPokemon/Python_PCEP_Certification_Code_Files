"""
Frage 53
Übersprungen
Q115

What is the output of the following code snippet?
-------------------------------------------------
Richtige Antwort
3 2
"""


def test(x=1, y=2): # x=1, y=2 bedeutet: Wenn du beim Aufruf keine Argumente übergibst, nimmt Python standardmäßig x=1 und y=2.
        x = x + y
        y += 1
        print(x, y)     # 3 2


test(5, 3)  # 3 2 | Wenn du die Funktion mit Argumenten aufrufst, werden diese Default-Werte überschrieben. | (die Default-Werte x=1, y=2 spielen hier keine Rolle mehr)

#Bsp.    
    # x = x + y       # 5 + 3 == 8 | x ist also 8
    # y += 1          # 3 + 1 == 4 | y ist also 4   