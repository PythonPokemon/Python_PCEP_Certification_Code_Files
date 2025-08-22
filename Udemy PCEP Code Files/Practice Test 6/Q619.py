
def func(n):
    s = '*'                  # Startwert s = '*'
    for i in range(n):       # Schleife i geht über 0 ... n-1
        s += s               # s wird verdoppelt: s = s + s
    yield s                  # Generator gibt s einmal aus
    # return s               # wäre normaler Rückgabewert, hier Generator



for x in func(2):           #  funktionsaufruf mit parameter angabe == 2 == **
    print(x, end='')        # da ** verdoppelt wird == ****

print()
print(func(2))        # <generator object func at ...>
print(list(func(2)))  # ['****']

s = '*'
s += s    #  '*' + '*'  == '**'
s += s    # '**' + '**' == '****'
print(s)  # ****
