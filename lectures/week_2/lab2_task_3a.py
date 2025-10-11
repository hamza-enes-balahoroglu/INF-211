"""
Task 3a: Ask for an input string from
the user and print the reverse of it. 
• inputs : input ∈ {x: printable 
characters except 

whitespaces and len(x) ∈ [1, 100]}. 
• output : string 
The output must be as follows: 
Enter a string: Inf211 
112fnI 
"""

text = input("Enter a text : ")

if len(text) >= 1 and len(text)<=100:
    # 2 alternatif
    print(text[::-1])
    print("".join(reversed(text)))
    pass