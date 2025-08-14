
nums = [1, 2, 3]
data = ('Peter',) * (len(nums) - nums[::-1][0])
print(data)  # ()

print(len(nums) - nums[::-1][0])            # 0
print(len([1, 2, 3]) - [1, 2, 3][::-1][0])  # 0
print(3 - [3, 2, 1][0])                     # 0
print(3 - 3)                                # 0
print(0)                                    # 0

print(('Peter',))        # ('Peter',)
print(type(('Peter',)))  # <class 'tuple'>
print(type('Peter'))     # <class 'str'>
print(('Peter',) * 0)    # ()
print((1, 2, 3) * 0)     # ()
