"""
start -1
stop -2
step keine
---------------------------------------------------------------------------
da stop hinter -1 liegt fängt die .len() methode garnicht erst an zu zählen
und bleibt bei null!
---------------------------------------------------------------------------
"""


L = [i for i in range(-1, -2)]
print(L)       # []
print(len(L))  # 0
