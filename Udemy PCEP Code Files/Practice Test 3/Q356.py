# methoden deklaration
var = 1     # variable wird der wert 1 zugewiesen

def any():
    print(var + 1, end='')  # var +1 == 2 end='' unterdrückt den Zeilenumbruch



any()       # methodenaufruf == 2
print(var)  # 1, da aber zeilenumbruch unterdrückt wird hinter der 2 ausgegeben 1 == 21
