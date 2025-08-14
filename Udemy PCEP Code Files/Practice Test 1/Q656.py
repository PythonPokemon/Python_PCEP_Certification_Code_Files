
# The return keyword forces the function's execution to terminate:
def my_function():
    print("Hello")
    return
    print("World")


my_function()  # Hello


# The return keyword may cause the function to return a value:
def my_function():
    return "Hello"


print(my_function())  # Hello
