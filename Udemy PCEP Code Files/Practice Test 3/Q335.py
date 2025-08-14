"""
ändere day = 'tag' zum teste
"""

day = 'Wednesday'       # such dir einen tag zum testen aus und schau ob unten die entsprechenden punkte ausgegeben werden.

discount = 0            # startpunkte

if day == 'Wednesday':
    discount += 5
elif day == 'Thursday':
    discount += 7
elif day == 'Saturday':
    discount += 10
elif day == 'Sunday':
    discount += 20
else:
    discount += 2

print(discount)         # ausgabe, der endpunkte!
