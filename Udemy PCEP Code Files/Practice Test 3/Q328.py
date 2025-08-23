"""
Was passiert hier?
1. ord() Funktion
ord(<Zeichen>) gibt den Unicode-Codepunkt (früher: ASCII-Wert bei Standardbuchstaben) zurück.
---------------------------------------------------------------------------------------------
hier werden die dezimal zahlen miteinander verrechnen und die summe ist 2

a == 97
c == 99
---------------------------------------------------------------------------------------------
c -a = 2
|  | = |
99-97= 2
---------------------------------------------------------------------------------------------
"""
print(ord('c') - ord('a'))  # 2 | 99 - 97 == 2
print(ord('c'))             # c entspricht decimal 99
print(ord('a'))             # a entspricht decimal 97
