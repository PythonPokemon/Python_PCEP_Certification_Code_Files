"""
Erklärung
1. Unterschied: Zahlen x Zahlen vs. String x Zahl
Zahlen x Zahlen → Mathematische Multiplikation

String x Zahl → String wird so oft wiederholt, wie die Zahl angibt
-------------------------------------------------------------------
Regeln in Python
-------------------------------------------------------------------
✅ erlaubt:
'Hi' * 4   # 'HiHiHiHi'
4 * 'Hi'   # 'HiHiHiHi'  (Reihenfolge egal)
-------------------------------------------------------------------
❌ nicht erlaubt:
'Hi' * 2.5  # TypeError (float geht nicht)
→ Hier müsste man erst int(2.5) machen.
-------------------------------------------------------------------
"""
x1 = '23'
y1 = 7
z1 = x1 * y1
print('23' * 7)  # '23232323232323'

x2 = 42
y2 = 7
z2 = x2 / y2
print(42 / 7)    # 6.0

x3 = 4.7
y3 = 1
z3 = x3 / y3
print(4.7 / 1)   # 4.7

print(type(z1))  # <class 'str'>
print(type(z2))  # <class 'float'>
print(type(z3))  # <class 'float'>
