
my_list = ['Mary', 'had', 'a', 'little', 'lamb']


def my_list(my_list):
    del my_list[3]
    # TypeError: 'function' object does not support item deletion
    my_list[3] = 'ram'
    # TypeError: 'function' object does not support item assignment


print(my_list(my_list))
