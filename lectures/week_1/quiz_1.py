# e üzeri x değerini yaklaşık olarak hesapla. (Nasıl hesaplanacağına dair formül verilir.)

result = 0
x = int(input("Number : "))

for n in range(0, 25):
    fac = 1
    for j in range(1, n+1):s
        fac *= j
        pass
    result += (x**n)/ fac
    pass

print(f"Result : {result}")