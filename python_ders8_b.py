#!/usr/bin/python3

from urun import urun1
from urun import elma
from funcs.test import ornek

ekmek = urun1()
benimelmam = elma()
ornektest = ornek()

print(ekmek.firma)
ekmek.firma = "Ay ekmek"
print("ekmek firması:",ekmek.firma)


print("elmanın rengi:",benimelmam.renk)


ornektest.bilgi="test"
print(ornektest.bilgi)
