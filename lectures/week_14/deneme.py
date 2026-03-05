def asallari_bul(sinir:int) -> list:
    asallar = []
    
    for sayi in range(2, sinir + 1):
        is_prime = True
        
        karekok_limit = int(sayi ** 0.5) + 1
        
        for i in range(2, karekok_limit):
            if sayi % i == 0:
                is_prime = False
                break
        
        if is_prime:
            asallar.append(sayi)
            
    return asallar

def en_yakın_ikilik_sayi(sayi):
    
    for i in range(0, sayi):
        if 2 ** i > sayi:
            return 2 ** i
    return 0

max_val = int(input("max val : "))

asallar = asallari_bul(max_val)

for i in asallar:
    ikilik_sayı = en_yakın_ikilik_sayi(i)
    fark = ikilik_sayı - i
    print(f"Sayı : {str(i).ljust(10, " ")}  Fark : {str(fark).ljust(10, " ")} İkilik sayı : {ikilik_sayı}")
    pass