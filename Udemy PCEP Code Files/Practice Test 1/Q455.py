"""
Frage 71
Übersprungen
Q455

What is the output of the following snippet?
--------------------------------------------
Richtige Antwort
4
--------------------------------------------
Erklärung:

Zuerst wird an die Funktion übergeben,3
1 wird hinzugefügt und zurückgegeben.4
Das wird zugeordnet und dann gedruckt.4x
--------------------------------------------
"""


def fun(x):
    x += 1
    return x


x = 2
x = fun(x + 1)
print(x)  # 4
