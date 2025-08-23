"""
 bei Tuples suchst du immer nach dem Positions/Wert, nicht nach einem Index.
"""
# Pos: 0  1  2
foo = (1, 2, 3)
print(foo.index(1)) # 0 | gibt an, wo bzw, an welcher position, sich der expliziter wert befindet in der tupel, nicht der index !
print(foo.index(2)) # 1 | gibt an, wo bzw, an welcher position, sich der expliziter wert befindet in der tupel, nicht der index !
print(foo.index(3)) # 2 | gibt an, wo bzw, an welcher position, sich der expliziter wert befindet in der tupel, nicht der index !

#foo.index(0)        # versucht einen Wert im Index position [0] zu finden | # ValueError: tuple.index(x)


