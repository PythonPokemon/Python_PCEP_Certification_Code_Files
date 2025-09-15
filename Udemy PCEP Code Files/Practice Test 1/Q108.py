"""
Frage 23
Übersprungen
Q108

What will be the output of the following code snippet?
Richtige Antwort
4
"""

d = {}      # erstellt ein dictionary
print(d)    # {}
d[1] = 1    # erstll ein key1:wert1
print(d)    # {1: 1}
d['1'] = 2
print(d)    # {1: 1, '1': 2}
d[1] += 1
print(d)    # {1: 2, '1': 2}

sum = 0
for k in d:
    sum += d[k]
    print("key: ", k, " - value: ", d[k])
    # key:  1  - value:  2
print(sum)  # 4

# sum = 0
# for k in d.keys():
#     sum += d[k]
#     print("key: ", k, " - value: ", d[k])
#     # key:  1  - value:  2
# print(sum)  # 4
