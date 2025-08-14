
x = (1, 4, 7, 9, 10, 11)
y = {2: 'A', 4: 'B', 6: 'C', 8: 'D', 10: 'E', 12: 'F'}
res = 1
for z in x:
    print('z in for:', z)
    # z in for: 1
    # z in for: 4
    # z in for: 7
    # z in for: 9
    # z in for: 10
    # z in for: 11
    if z in y:
        print('z in if:', z)
        # z in if: 4
        # z in if: 10
        res += z
print(res)              # 15
