"""
Frage 93
Übersprungen
Q318

What is the expected output of the following code?
print(2 ** 3 ** 2 ** 1)
--------------------------------------------------
Richtige Antwort
512
"""

#               2 *  1 = 2
#          3 *  2 =  9                                                        4   8   16  32  64  128 256 512
#     2 ** 9                2 hoch 9                                      |   |   |   |   |   |   |   |   |  == 9
print(2 ** 3 ** 2 ** 1)    # 512 | 2 ** 3 ** | 2 *1 = 2 | 3 * 2 = 9 | 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2  == 512
print(2 ** 3 ** (2 ** 1))  # 512
print(2 ** 3 ** 2)         # 512
print(2 ** (3 ** 2))       # 512
print(2 ** 9)              # 512
print(512)                 # 512
