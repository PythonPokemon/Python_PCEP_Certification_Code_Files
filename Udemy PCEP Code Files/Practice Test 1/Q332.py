
import sys
print(sys.argv[0])  # The first index is the name of the file

# Now execute the following to create the needed file:
code = '''
import sys
for a in sys.argv[1:]:
    print(a)
'''
with open('argv.py', 'w') as f:
    f.write(code)

# In Terminal:
# python argv.py Peter Paul Mary

"""
Peter
Paul
Mary
"""
