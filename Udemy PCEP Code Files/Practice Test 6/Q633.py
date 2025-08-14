
# x, y = eval(input('Enter two numbers: '))
x, y = eval('3, 4')              # works
# x, y = eval('3 4')             # SyntaxError: ...
# x, y = eval('<pre>3 4</pre>')  # SyntaxError: ...
print(x)  # 3
print(y)  # 4
