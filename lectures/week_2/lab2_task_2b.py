"""
Task 2b: Each Lucas  number is defined to be the sum  of its two immediate previous terms 
and the first two Lucas numbers are L(0) = 2, and L(1) = 1 as shown below.  [2] 
𝑳𝒏 ={
𝟐               𝒊𝒇 𝒏 =𝟎
𝟏               𝒊𝒇 𝒏 =𝟏
𝑳𝒏−𝟏 +𝑳𝒏−𝟐      𝒊𝒇 𝒏> 𝟏
 
Ask for a  number from the user.  Calculate and  print the lucas number that corresponds to 
that number starting with index 0. As an example, first 7 Lucas numbers are: 2, 1, 3, 4, 7, 11, 
18. 
• inputs : input = {x: x ∈ ℕ and 1E6 ≥ x ≥ 0} 
• output : integer 

"""

n               = int(input("Number  : "))
previous_val1   = 0
previous_val2   = 0
result          = 0

if  n>=0:
    for i in range(n+1):
        
        if i == 0:
            result = 2
            pass
        elif i == 1:
            result = 1
            previous_val1 = 2
        else:
            previous_val2 = previous_val1
            previous_val1 = result
            result = previous_val1 + previous_val2
            pass
    pass
else:
    print("Invalid Number")
    pass

print(result)