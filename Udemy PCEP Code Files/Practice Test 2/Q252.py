
dictionary = {}
my_list = ['a', 'b', 'c', 'd']


for i in range(3):                          # i iteriert durch die angegeben listen [a,b,c] == indemfall 3, weil 3 angegeben wurde
    dictionary[my_list[i]] = (my_list[i], )
print(dictionary)                           # {'a': ('a',), 'b': ('b',), 'c': ('c',)}


for i in dictionary.keys():                 # i iteriert durch die dictionarys und merkt sich die keys
    k = dictionary[i]                       # k bekommt den wert der keys zugewiesen
                                            # print(k)  # ('a',) ('b',) ('c',)
                                            # print(k['0'])  # TypeError: tuple indices must be integers or slices, not str
                                            # print(k["0"])  # TypeError: tuple indices must be integers or slices, not str
    print(k[0])
"""
a
b
c
"""