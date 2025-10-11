# -*- coding: utf-8 -*-
# Date  :  10.10.2025
"""
- continue yapısı dögünün onaylanmasını sağlar
döngü onaylanır ve sonraki dögüye geçilir.

- örnekte döngü 4'te onaylanır ve sonraki
sayıyı yazdırmak üzere sıradaki döngüye 
girer. Çıktıda 4 olmaz.
"""

for i in range(1,11):
    if i == 4:
        continue
    print(str(i).center(16, " "))
    pass

print("_" * 16)


"""
- break döngüyü kople bitirir. 4 değerine
ulaşıldığında for döngüsü tamamen bitmiş
sayılır
"""

for i in range(1,11):
    if i == 4:
        break
    print(str(i).center(16, " "))
    pass