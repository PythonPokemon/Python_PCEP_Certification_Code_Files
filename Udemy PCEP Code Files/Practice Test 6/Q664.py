
try:
    # number = input('Please enter a number\n')
    number = 'one'      # wenn man in den string statt: 'one' eine '1' schreibt wird die zahl übernommen!
    zahl = int(number)  # hier ist zwar eine typumwandlung von string zu int, aber oben wird dennoch ein string erzeugt
    print('Perfekt!')
except:                 # eception handling == hier wird der fehler abgefangen und eine nachricht erzeugt!
    print('Something went wrong.')

