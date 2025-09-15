"""
Frage 167
Übersprungen
Q332
By which variable of the sys module can we access command line arguments?

Richtige Antwort
argv
"""
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
