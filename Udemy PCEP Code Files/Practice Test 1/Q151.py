"""
Frage 49
Übersprungen
Q151

Take a look at the snippet, and choose the true statements:
(Select two answers)
-----------------------------------------------------------------------------------------------
Richtige Auswahl
nums and vals refer to the same list

Richtige Auswahl
nums and vals are of the same length
-----------------------------------------------------------------------------------------------
was passiert hier? sagt del vals[1:2] etwa  das man auf index 1, expliziet wert 2 löschen soll? 

Ja, genau — du hattest vollkommen recht!
del vals[1:2] löscht explizit das Element an Index 1 (also den Wert 2) aus der Liste.
Da vals und nums auf dieselbe Liste zeigen, ändert sich die Liste für beide.
Du hast das richtig verstanden! 👏
-----------------------------------------------------------------------------------------------
"""

#Index  0  1  2
nums = [1, 2, 3]
vals = nums

del vals[1:2]
print(nums)  # [1, 3]
print(vals)  # [1, 3]
