
my_list = [1, 2]

for v in range(2):
    my_list.insert(-1, my_list[v])

print(my_list)  # [1, 1, 1, 2]

# The same without for loop:
my_list_2 = [1, 2]
my_list_2.insert(-1, my_list_2[0])
print(my_list_2)  # [1, 1, 2]
my_list_2.insert(-1, my_list_2[1])
print(my_list_2)  # [1, 1, 1, 2]
