# -*- coding: utf-8 -*-
# Date  :  10.10.2025

"""

"""

guess   = int(input("Enter an guess    : "))

num     = int(input("Enter an integer  : "))

while guess**2 <= num:
    print(f"Guess : {guess}")
    
    if(guess**2 == num):
        print(f"Square root of {num} is {guess}")
        break
    
    else:
        guess += 1
        pass
    
else:
    print(f"{num} sayısının yaklaşık karekökü {guess}")  # ingilizcem yetmedi
