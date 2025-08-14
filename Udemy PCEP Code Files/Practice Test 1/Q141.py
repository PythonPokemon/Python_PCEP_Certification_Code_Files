"""
Das ist ein schönes kleines Beispiel, das drei Python-Konzepte auf einmal zeigt:
Listen-/String-Slicing mit Schrittweite
Generatoren mit yield
Iteration mit for
------------------------------------------------------------------------------------
data[::2] bedeutet:

    Start: nicht angegeben → beginnt bei Index 0
    Ende: nicht angegeben → geht bis zum Ende der Sequenz
    Schrittweite = 2 → nimmt jedes zweite Zeichen
    Beispiel: "abcdef"[::2] → ['a', 'c', 'e']
------------------------------------------------------------------------------------
yield bedeutet:

Die Funktion ist ein Generator → sie gibt nicht alles auf einmal zurück, sondern ein Element pro Durchlauf.
Jeder yield pausiert die Funktion und gibt einen Wert zurück, bis der nächste Wert angefordert wird.

💡 Merksatz:
yield = "Ich gebe dir das nächste Stück, aber behalte den Rest im Ofen, bis du danach fragst."
"""
def func(data):
    for d in data[::2]: # startwert index 0, da nichts angegeben, aber schritweite 2
        yield d         # gibt jedes Element zurück, pro Durchlauf.

# hier wird die vordefinierte Funktion aufgerufen, mit neuen Daten als Argument
# und die for-Schleife iteriert über die Werte, die yield zurückgibt.
for x in func('abcdef'):
    print(x, end='')  # ace

"""
func('abcdef') erzeugt einen Generator, der 'a', 'c' und 'e' nacheinander liefert.
Die for-Schleife holt sich diese Werte in der Reihenfolge, in der yield sie bereitstellt.
end='' sorgt dafür, dass print keinen Zeilenumbruch macht → alles steht in einer Reihe.
------------------------------------------------------------------------------------
ohne end='' würde jeder Buchstabe in einer neuen Zeile ausgegeben werden.
a
c
e
"""