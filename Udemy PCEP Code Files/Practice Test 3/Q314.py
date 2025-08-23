"""
neuer Index wird hinzugefügt!
"""
def func(item):
    item += [1]     # [1, 2, 3, 4] + [1] -> [1, 2, 3, 4, 1]


data = [1, 2, 3, 4]
func(data)          # funktion greift auf data liste zu und wird ausgeführt, was bedeutet das ein neues item, hier der wert 1, der liste hinzugefügt wird.
print(len(data))    # gibt die länge aus der enhaltenen elemente in der iste == 5

print("Testaufruf des neuen eintrags auf Index[4] sollte 1 sein == ", data[4])      #
print(data)         # [1, 2, 3, 4, 1]

# separates beispiel
x = [1, 2, 3, 4]
x.append(1)         # fügt ein einzelnes element am ende der liste hinzu
x.append([1, 2])    # fügt am ende der liste ein list mit zwei elementen hinzu
x.extend([7])       # extend() entpackt die Elemente der übergebenen Liste und fügt sie einzeln hinzu.
print(x)            # [1, 2, 3, 4, [1]]
