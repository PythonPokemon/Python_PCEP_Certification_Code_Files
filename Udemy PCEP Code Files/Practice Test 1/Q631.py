
# First execute the following to create the needed file:
code = '''
from sys import argv
print(argv[1])
'''
with open('index.py', 'w') as f:
    f.write(code)

# In Terminal:
# python index.py Hello
