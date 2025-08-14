
def fun(a, b, c=0):
    # Body of the function.
    pass


fun(b=0, a=0)
fun(0, 1, 2)
# fun()     # TypeError: fun() missing 2 required positional arguments: 'a' and 'b'
# fun(b=1)  # TypeError: fun() missing 1 required positional argument: 'a'
