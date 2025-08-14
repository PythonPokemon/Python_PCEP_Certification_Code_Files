"""
Der Code nutzt den Bitshift-Operator <<, um den Wert von x bei jedem Schleifendurchlauf zu verdoppeln.
also im binär system mit 2er potenzen
                                                HD    2K    4K    8K
0   1   2   4   8   16  32  64  128  256  512  1024  2048  4096  8192

Und jeder durchlauf wird um eine potenz erhöht im binär system solnage kleiner 10 ist!
also als es bei 16 ankam vergleich kleiner 10, stop!

| Schritt | Binär vorher | Operation | Binär nachher | Dezimalwert                  |
| ------- | ------------ | --------- | ------------- | ---------------------------- |
| 1       | `0001` (1)   | `<< 1`    | `0010`        | 2                            |
| 2       | `0010` (2)   | `<< 1`    | `0100`        | 4                            |
| 3       | `0100` (4)   | `<< 1`    | `1000`        | 8                            |
| 4       | `1000` (8)   | `<< 1`    | `10000`       | 16 (Abbruch, weil `x >= 10`) |
| ------- | ------------ | --------- | ------------- | ---------------------------- |

Potenz     Dezimal    Binär     
--------------------------------
2^0        1          00000001
2^1        2          00000010
2^2        4          00000100
2^3        8          00001000
2^4        16         00010000

"""
x = 1
while x < 10:
    print('*')
    x = x << 1                  # Bitshift-Operator <<, um den Wert von x bei jedem Schleifendurchlauf zu verdoppeln.
    print('x:', x)              # von 1 auf 2 -> 4 -> 8 -> 16   usw....
    print('bin(x):', bin(x))    # 0b10->0b100->0b1000->0b10000


