"""
------------------------------------------------------------------------------------------
| Feature        | Verhalten                                                             |
| -------------- | --------------------------------------------------------------------- |
| `for ... else` | else läuft, wenn Schleife **ohne break beendet** wird                 |
| `break`        | verhindert die Ausführung des `else`                                  |
| Kein `break`   | `else` wird immer ausgeführt, **auch wenn Schleife nur einmal läuft** |
------------------------------------------------------------------------------------------
💡 Merksatz:

else bei Schleifen ist kein "sonst" wie in if, 
sondern läuft nur, wenn die Schleife nicht durch break beendet wird
------------------------------------------------------------------------------------------
"""

for i in range(1):
    print('*')      # *
else:
    print('*')      # *
