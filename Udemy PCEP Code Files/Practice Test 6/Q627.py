"""
Ternary-Operatoren 
"""
x = 42
y = 7
data = "I'm gonna make him an offer he can't refuse." # 43 Zeichen inklusive leerzeichen

print(data.find('an') if data else None)   # 19 | erster 'an'
print(19 if None else x / y)               # 42 / 7 == 6.0
print(data.rfind('an') if data else None)  # 32 | letzter 'an'
print(7 if len(data) > 19 else 6)          # 7  | wenn länge data 43 größer 19 ist, sonst 6
