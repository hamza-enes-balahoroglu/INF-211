# -*- coding: utf-8 -*-
# Date  :  10.10.2025

"""

"""


cube = int(input("Enter an integer  : "))
not_perfect = 0
for guess in range(abs(cube)+1):    # abs() mutlak değer
    if guess**3 == abs(cube):
        if cube < 0:
            guess *= -1
            pass
        print(f"Cube root of {cube} is {guess}.")
        break
    elif guess**3 > cube:
        not_perfect = guess
        break
    
if not_perfect != 0:
    print(f"Not perfect cube root of {cube} is {guess}")
    pass