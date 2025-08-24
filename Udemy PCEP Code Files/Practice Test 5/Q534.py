
data = ['Peter', 'Paul', 'Mary', 'Jane']

"""
-----------------------------------------
| i       | in data? | res nach Schritt |
| ------- | -------- | ---------------- |
| 'Peter' | ja       | 0                |
| 'Steve' | nein     | 0 + 100 = 100    |
| 'Jane'  | ja       | 0                |
-----------------------------------------
"""
res = 0
for i in ('Peter', 'Steve', 'Jane'):    # Prüft für jedes Element, ob es nicht in der Liste data vorkommt
    if i not in data:
        res += 100
print(res)  # 100                       | Nur 'Steve' ist nicht in data → res wird einmal um 100 erhöht

# -------------------------------------------------------------------------------------------------------

"""
-----------------------------------------
| i       | in data? | res nach Schritt |
| ------- | -------- | ---------------- |
| 'Peter' | ja       | 0 + 50 = 50      |
| 'Steve' | nein     | 0                |
| 'Jane'  | ja       | 0 + 50 = 50      |
-----------------------------------------
"""
res = 0
for i in ('Peter', 'Steve', 'Jane'):
    if i in data:
        res += 50
print(res)  # 100 | + 50 Peter + 50 Jane == 100

# -------------------------------------------------------------------------------------------------------
"""
-----------------------------------------
| i       | in data? | res nach Schritt |
| ------- | -------- | ---------------- |
| 'Peter' | ja       | 0 + 100 = 100    |
| 'Steve' | nein     | 0                |
| 'Jane'  | ja       | 0 + 100 = 100    |
-----------------------------------------
"""
res = 0
for i in ('Peter', 'Steve', 'Jane'):
    if i in data:
        res += 100
print(res)  # 200

# -------------------------------------------------------------------------------------------------------
"""
-----------------------------------------
| i       | in data? | res nach Schritt |
| ------- | -------- | ---------------- |
| 'Peter' | ja       | 0                |
| 'Steve' | nein     | 0 + 50 = 50      |
| 'Jane'  | ja       | 0                |
-----------------------------------------
"""
res = 0
for i in ('Peter', 'Steve', 'Jane'):
    if i not in data:
        res += 50
print(res)  # 50
