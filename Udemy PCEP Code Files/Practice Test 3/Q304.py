"""
--------------------------------------------------------------------------------------------------
Inklusive         Excklusive (bedeutet bis zur genannten Zahl, aber sie nicht mit einschließen)!
    |                  |
    ------       -------
          |     |
        start|stop|schrittweite
        -1   |  2 | default 1

zudem bsp. (-1, 2)
--------------------------------------------------------------------------------------------------
"""

data = [i for i in range(-1, 2)]

# Index indemfall              0  1  2 == länge 3
#                              |  |  |
print(data)                # [-1, 0, 1]
print(len(data))           # 3 

print(list(range(-1,2)))  # [-1, 0, 1]
