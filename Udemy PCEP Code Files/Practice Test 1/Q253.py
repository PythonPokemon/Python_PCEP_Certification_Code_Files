
my_list = [x * x for x in range(5)] # multipliziert  die werte aus der liste mit sich selbst: 0,1,2,3,4
print(my_list)  # [0, 1, 4, 9, 16]
# The same without list comprehension:

my_list = []
for x in range(5):
    my_list.append(x * x)
print(my_list)  # [0, 1, 4, 9, 16]

def fun(lst):
    # del lst[lst[2]]
    print(lst[2])  # 4
    del lst[4]
    return lst

print(fun(my_list))  # [0, 1, 4, 9]


print(my_list[2])  # 4
print(4)           # 4

print(my_list[my_list[2]])  # 16
print(my_list[4])  # 16



