
my_list = [1, 2]

for v in range(2):
    my_list.insert(-1, my_list[v])  # vor dem letzten index also: [1,hier, 2] werden erneut die zahlen aus der liste eingefügt!

print(my_list)  # [1, 1, 1, 2]


my_list_2 = [1, 2]
my_list_2.insert(-1, my_list_2[0])
print(my_list_2)  # [1, 1, 2]
my_list_2.insert(-1, my_list_2[1])
print(my_list_2)  # [1, 1, 1, 2]
