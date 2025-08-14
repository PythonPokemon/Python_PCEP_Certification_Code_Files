"""
Merke:

sep=" 🍎 " wirkt nur zwischen den Argumenten, nicht davor oder danach.
Du kannst auch längere Strings oder sogar Emojis als Separator verwenden:
"""
z = y = x = 1
print(x, y, z, sep='*')  # 1*1*1
print(x, y, z, sep=' ')  # 1 1 1
print(x, y, z)           # 1 1 1
