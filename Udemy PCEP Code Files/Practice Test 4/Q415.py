"""
Alles klar! Das ist ein kleines Beispiel zu bitweisen Operatoren in Python. 
Lass uns das Schritt für Schritt durchgehen. 🐍
---------------------------------------------------------------------------
1️⃣ Die Operatoren
Operator	Bedeutung
&	            AND - beide Bits müssen 1 sein
`	            `
^	            XOR - genau ein Bit ist 1

Hier behandeln wir Zahlen als Binärwerte, z.B. 
1 = 0b1, 
0 = 0b0.
"""
a = 1  # 0b1
b = 0  # 0b0

c = a & b  # 0b1 AND 0b0 = 0b0 → 0
d = a | b  # 0b1  OR 0b0 = 0b1 → 1
e = a ^ b  # 0b1 XOR 0b0 = 0b1 → 1

print(c + d + e)  # 0 + 1 + 1 = 2


print(1 & 0)      # 0 
print(1 | 0)      # 1 
print(1 ^ 0)      # 1
