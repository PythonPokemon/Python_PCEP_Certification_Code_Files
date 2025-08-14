"""
Das global y sorgt dafür, dass die Variable y nicht nur innerhalb der Funktion func() existiert, 
sondern im globalen Namensraum des Programms angelegt oder verändert wird.

1.Ohne global würde y eine lokale Variable in func() sein → außerhalb nicht sichtbar.
2.Mit global y sagst du Python: „Wenn es y schon global gibt, benutze diese; wenn nicht, lege sie global an.“
3.Wenn du dann func(2) aufrufst, wird:
4.y = 4 global gespeichert.

Danach kannst du außerhalb der Funktion direkt print(y) machen.
"""

def func(x):
    global y
    y = x * x
    return y


func(2)
print(y)  # 4
