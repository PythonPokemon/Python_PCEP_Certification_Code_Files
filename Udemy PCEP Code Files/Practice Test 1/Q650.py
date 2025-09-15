"""
Frage 11
Übersprungen
Q650

What is the output of the following snippet?
Richtige Antwort
[3, 2, 1]
"""

my_list_1 = [1, 2, 3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v)
print(my_list_2)  # [3, 2, 1]
