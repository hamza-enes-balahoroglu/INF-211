import math

r =  int(input("Radus : "))
h = int(input("Height : "))

print(f"Volume = {math.pi * (r**2) * h:.2f}")


number = input("Okul numaranızı giriniz : ")
toplam = 0

for i in number:
    toplam += int(i)
    pass
print(f"Elemanlar toplamı : {toplam}")

my_name = "Hamza"

start = int(input("Start at : "))
stop  = int(input("Stop at  : ")) + 1

print(my_name[start:stop])

tag = {'a','b','c'}

raw = input("Text git : ")

counter = 0

for i in raw:
    for j in tag:
        if(i == j):
            counter += 1
        pass
    pass

print(counter)

num = int(input("Sayı giriniz  : "))+1
result = 1
for i in range(1, num):
    result *= i
    pass
print(f"Çarpım = {result}")
