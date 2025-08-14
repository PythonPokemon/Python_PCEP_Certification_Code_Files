
list = [False, True, "2", 3, 4, 5]
b = 0 in list
print(b)  # True

# The same without the in operator:
list2 = [False, True, "2", 3, 4, 5]
res = False
for i in list2:
    if i == 0:
        res = True
print(res)  # True

print(0 == False)  # True | weil 0 == False entspricht



