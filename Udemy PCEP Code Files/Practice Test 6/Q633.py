"""
Erklärung:

eval() ist eine eingebaute Python-Funktion.
Sie wertet einen String so aus, als wäre es Python-Code.
Das heißt: Der String '3, 4' wird von eval wie echtes Python behandelt.
-----------------------------------------------------------------------
Schritt für Schritt:

'3, 4' ist im String.
eval('3, 4') → Python interpretiert das wie:

(3, 4)
also ein Tuple mit zwei Werten.

Links steht x, y → sogenanntes Tuple Unpacking:
"""


x, y = eval(input('gib zwei nummern ein: '))  # achtung komma getrennt
x, y = eval('3, 4')              # 
# x, y = eval('3 4')             # SyntaxError: ...
# x, y = eval('<pre>3 4</pre>')  # SyntaxError: ...
print(x)  # 3
print(y)  # 4
