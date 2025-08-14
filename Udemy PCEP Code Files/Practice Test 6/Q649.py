
vals = [0, 1, 2]
vals[0], vals[1] = vals[1], vals[2]
print(len(vals))  # 3
print(vals)       # [1, 2, 2]
