"""
Frage 111
Übersprungen
Q651

What is the output of the following snippet?
--------------------------------------------
Richtige Antwort
no output, the snippet is erroneous
"""


my_list = ['Mary', 'had', 'a', 'little', 'lamb']   # eine Liste mit 5 Strings



def my_list(my_list):                              # ❌ Funktionsname = gleicher Name wie die Variable
    del my_list[3]                                 # versucht: Element an Index 3 löschen
    my_list[3] = 'ram'                             # versucht: Element an Index 3 ändern
"""
➡️ Hier passiert der Fehler:
Die Variable my_list (Liste) wird durch die Funktion my_list() überschrieben.
Ab dem Zeitpunkt, wo die Funktion definiert ist, verweist my_list im globalen Scope nicht mehr auf die Liste, sondern auf die Funktion selbst.
"""
print(my_list(my_list))                             # versucht, die Funktion aufzurufen

"""
Jetzt wird my_list als Funktion aufgerufen.
Das Argument my_list (die Funktion selbst) wird übergeben.
In der Funktion bedeutet del my_list[3] → versuch, Index 3 einer Funktion zu löschen.

Ergebnis:
TypeError: 'function' object does not support item deletion

✅ Erklärung, warum „erroneous“
Der Fehler ist Namenskonflikt: Funktionsname = Variablenname.
Dadurch überschreibt die Funktion die ursprüngliche Liste.
Deshalb ist das Snippet fehlerhaft und produziert keine Ausgabe.
"""



# 👉 Lösung wäre, der Funktion einen anderen Namen zu geben:
#Index:           0      1     2      3         4
meine_liste = ['Mary', 'had', 'a', 'little', 'lamb']

def ändere_liste(meine_liste):      # übergiebtr der funktion die Liste als argument
    del meine_liste[3]              # löscht in der liste das element auf Index[3] == ['Mary', 'had', 'a', 'lamb']
    meine_liste[3] = 'ram'          # weist der liste einen neuen wert auf den Index[3] zu == ['Mary', 'had', 'a', 'ram', 'lamb']
    return meine_liste              # gibt die liste als argument zurück

print(ändere_liste(meine_liste))    # ruft funktion auf ['Mary', 'had', 'a', 'ram', 'lamb']

