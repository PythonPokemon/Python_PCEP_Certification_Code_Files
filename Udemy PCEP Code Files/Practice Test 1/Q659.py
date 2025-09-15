"""
Frage 197
Übersprungen
Q659
Which one of the lines should you put in the snippet below to match the expected output?

Expected output:
[1, 2, 4, 7]


Code:
list = [2, 7, 1, 4]
 
# enter code here
 
print(list)

Richtige Antwort
list.sort()

Erklärung
The correct choice is to use `list.sort()` as it sorts the elements of the list in place, which means the original list is modified. This will rearrange the elements in ascending order, resulting in the expected output [1, 2, 4, 7].

"""


list = [2, 7, 1, 4]
list.sort()
print(list)  # [1, 2, 4, 7]
