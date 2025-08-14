
def fun(x, y, z):
    return x + 2 * y + 3 * z


print(fun(0, z=1, y=3))  # 9

print(0 + 2 * 3 + 3 * 1)      # 9 | 0 + 6 + 3 == 9
print(0 + (2 * 3) + (3 * 1))  # 9
print(0 + 6 + (3 * 1))        # 9
print(0 + 6 + 3)              # 9
print(6 + 3)                  # 9
print(9)                      # 9
