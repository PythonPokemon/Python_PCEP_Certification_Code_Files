"""
die zahlen in der list werden durch 2 geteilt in einer ganzzahl division! und rest soll 0 sein!

1 geteilt durch 2 ist 0,5 Rest = 0,5 | ungerade
2 geteilt durch 2 ist 1 Rest = 0 | gerade
3 geteilt durch 2 ist 1 Rest = 1 | ungerade
4 geteilt durch 2 ist 2 Rest = 0 | gerade
5 geteilt durch 2 ist 2 Rest = 1 | ungerade
6 geteilt durch 2 ist 3 Rest = 0 | gerade
7 geteilt durch 2 ist 3 Rest = 1 | ungerade
8 geteilt durch 2 ist 4 Rest = 0 | gerade 
9 geteilt durch 2 ist 4 Rest = 1 | ungerade
10 geteilt durch 2 ist 5 Rest = 0 | gerade

a = 5 % 2
print(a)

"""

x = 0
while x < 6:
    print('1. x:', x)         # 0 -> 1 -> 2 -> 3 -> 4 -> 5
    x += 1
    print('2. x:', x)         # 1 -> 2 -> 3 -> 4 -> 5 -> 6
    if x % 2 == 0:
        print('x in if:', x)  # 2 -> 4 -> 6
        continue
    print('x behind if:', x)  # 1 -> 3 -> 5
    print('*')
"""
*
*
*
"""

