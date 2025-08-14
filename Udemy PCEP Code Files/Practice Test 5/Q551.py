
my_tuple = (1, 2, 3, 4)
# Indexing:
print(my_tuple[2])  # 3
# Slicing:
print(my_tuple[1:3])  # (2, 3)

# They CANNOT be modified using the del instruction:
# del my_tuple[0]
# TypeError: 'tuple' object doesn't support item deletion

# They CANNOT be extended using the .append() method:
# my_tuple.append(5)
# AttributeError: 'tuple' object has no attribute 'append'
