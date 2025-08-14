"""
Letzte WIEDERHOLUNG: 314
-------------------
Practice Test 2:
238
239
252
257
-------------------
Practice Test 3:
304
305
309
-------------------
Practice Test 4:

-------------------
Practice Test 5:

-------------------
"""


for zahl in range(1, 11):  # Zahlen von 1 bis 10
    if zahl % 2 == 0:      # Modulo 2 ergibt 0 → gerade Zahl
        print(zahl, "ist gerade")
    else:                  # sonst → ungerade Zahl
        print(zahl, "ist ungerade")

# test einzelner Modulo operationen!
a = 5 % 2
print(a)