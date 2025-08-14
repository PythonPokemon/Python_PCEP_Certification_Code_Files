
vals = [0, 1, 2]
vals.insert(0, 1)
print(vals)  # [1, 0, 1, 2]
del vals[1]
print(vals)  # [1, 1, 2]
print(sum(vals))  # 4
