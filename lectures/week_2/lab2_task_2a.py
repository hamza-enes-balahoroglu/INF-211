# -*- coding: utf-8 -*-
"""
Task 2a: The 𝒏th  hexagonal number 𝒉𝒏  is the number 
of distinct dots in  a pattern of  dots 
consisting of  the outlines of regular hexagons with 
sides up to  𝒏  dots, when the hexagons 
are overlaid so that they share one vertex. [1]  
 
 
The formula for the 𝒏th hexagonal number is given as: 

𝒉𝒏 = 𝟐𝒏𝟐 −𝒏 
Ask for a number from the user. Calculate and print
the hexagonal number that corresponds 
to that number. As an example, first 7 hexagonal
numbers are: 1, 6, 15, 28, 45, 66, 91 . 
• inputs : input = {x: x ∈ ℕ and 1E6 ≥ x ≥ 1} 
• output : integer 
The output must be as follows: 
Enter a number: 1 
1 
>>> 
Enter a number: 6 
66 
"""

n = int(input("Enter a number : "))

hn = 2*(n**2) - n
print(f"Hexagonal number : {hn}")
