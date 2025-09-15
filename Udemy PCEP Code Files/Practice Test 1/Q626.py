"""
Frage 42
Übersprungen
Frage 626

Welches Snippet würden Sie in die unten angegebene Zeile einfügen, um es zu drucken?
The highest number is 10 and the lowest number is 1. an den Monitor?



data = [10, 2, 1, 7, 5, 6, 4, 3, 9, 8]
# insert your code here
print(
    ('The highest number is {} ' +
     'and the lowest number is {}.').format(high, low)
)
------------------------------------------------------------------------------------
Richtige Antwort:

def find_high_low(nums):
    nums.sort()
    return nums[-1], nums[0]
 
 
high, low = find_high_low(data)
"""

data = [10, 2, 1, 7, 5, 6, 4, 3, 9, 8]


def find_high_low(nums):        # funktion mit parameter nums
    nums.sort()                 # nums ruft die funktion .sor() auf die die elemente in der liste data = [10, 2, 1, 7, 5, 6, 4, 3, 9, 8] sortiert == data [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    print(nums)                 # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] nachdem die liste sortiert wurde :-)
    return nums[-1], nums[0]    # gibt das letzte element aus: nums[-1] == 10 | gibt das erste element aus:nums[0]
    


high, low = find_high_low(data) # hier wird die funktion den variabeln zugewiesen == high, low und es müssen zwei variablen sein, weil die funktion oben 2 werte returnt return nums[-1], nums[0] 
                                # außerdem wird der funktion == find_high_low(data) == data als argument überegen die die liste enthält == data = [10, 2, 1, 7, 5, 6, 4, 3, 9, 8]
print(
    ('The highest number is {} ' + 'and the lowest number is {}.').format(high, low)
)
# The highest number is 10 and the lowest number is 1.

"""
{} → Platzhalter

Die geschweiften Klammern sind Platzhalter, in die später Werte eingefügt werden.

Erstes {} wird durch high ersetzt
Zweites {} wird durch low ersetzt
------------------------------------------------------------------------------------
.format(...)

Die Methode .format() 
ersetzt die Platzhalter in der Zeichenkette durch die angegebenen Werte.
------------------------------------------------------------------------------------
"""