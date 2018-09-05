# -*- coding: utf-8 -*-

"""
**TIL ALLE**
Så norske tegn er ikke støttet i python!
HVIS det funker for deg, så er det fordi du bruker et program som fikser det!
Jeg vet ikke hvilke program som fikser det, men atom og sublime, som jeg bruker,
fikser det ikke!

HVIS du absolutt må skrive norsk i programmet ditt, så må du skrive denne linjen
øverst i programmet:
"""

# -*- coding: utf-8 -*-




# ENKELTE av dere greier ikke å bruke % (eventuelt .format):


a = 1.123456789
print("%.2f" % a,"euro") #NEI
print("%g euro" % a) #NEI, fordi dette ikke gir riktig antall desimaler
print("%.2f euro" % a) #JA, tallet to kan dere bytte med så mange desimaler dere vil ha


"""
tips til neste uke:
https://github.com/erikfsk/in1900/blob/master/week2_lister.py
"""