
try:
    number = 'one'      # teste statt 'one' | 1
    zahl = int(number)  # da hier string zu int umgewandelt wird!
    print('Perfekt!')
except:
    print('Something went wrong.')
    

# zahl = int('one')  # ValueError: ...
