"""
zwar wird der string in ein int umgewandelt aber dennoch als buchstabe 'one'
erwartet wird tatsächlich eine zahl! == bsp. 1

"""



try:
    user_input = 'one'          # 'one' == falsche wert zuweisun!
    num = 100 / int(user_input)
except ValueError:
    print('You need to use digits!')
except:
    print('Error')
else:
    print('Result:', num)

