
l1 = [1, 2, 3]
# for v in range(len(l1)):
for v in range(3):
    l1.insert(1, l1[v])
print(l1)  # [1, 1, 1, 1, 2, 3]

l2 = [1, 2, 3]
l2.insert(1, l2[0])
print(l2)  # [1, 1, 2, 3]
l2.insert(1, l2[1])
print(l2)  # [1, 1, 1, 2, 3]
l2.insert(1, l2[2])
print(l2)  # [1, 1, 1, 1, 2, 3]
