"""
Letzte WIEDERHOLUNG: 160 | 435
-------------------
Practice Test 2:
238
239
252
257
-------------------
Practice Test 3:
304
309
-------------------
Practice Test 4:

-------------------
Practice Test 5:

-------------------
"""

try:
    value = input("Enter a value: ")
    print(value/value)
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")