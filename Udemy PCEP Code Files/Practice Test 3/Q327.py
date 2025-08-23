"""
Kurzfassung:

1j ist in Python die komplexe Zahl mit imaginärem Teil 1.
type(1j) → <class 'complex'>
c.real → realer Teil (0.0)
c.imag → imaginärer Teil (1.0)
-----------------------------------------------------------------------------------
Mini-Erklärung für Teilnehmer
„Python unterstützt komplexe Zahlen direkt. 1j ist die imaginäre Einheit. 
Jede komplexe Zahl hat einen realen Teil (.real) und einen imaginären Teil (.imag). 
So können wir mathematische Berechnungen mit komplexen Zahlen durchführen.“
"""


print(type(1J))      # <class 'complex'>

c = 1j              # +1 imaginär durch zuwesiung
print(c.real)        # 0.0
print(c.imag)        # 1.0 imaginär durch zuwesiung | c = 1j  

# Alternative Schreibweise
print(type(0 + 1j))  # <class 'complex'>

