# 1. Quiz 
"""
Girilen metini ortadan iki parçaya ayıtrıp
oluşan 2 parçayı ters çevirip birleştiriniz.

Örnek :
system ==> sysmet
signal ==> gislan

"""

text  = input("Enter a text :")

a = text[0:len(text)//2]
a = a[::-1]
b = text[len(text)//2:]
b = b[::-1]
print(a+b)