
def function_1(a):
    return None


def function_2(a):
    return function_1(a) * function_1(a)
    # TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'


print(function_2(2))

print(None * None)
# TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'
