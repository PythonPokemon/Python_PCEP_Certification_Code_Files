
my_list = [1, 2, 3]


def delete_first(x):
    del x[0]        # löscht den wert im index[0], also 1


delete_first(my_list)
print(my_list)  # [2, 3]
