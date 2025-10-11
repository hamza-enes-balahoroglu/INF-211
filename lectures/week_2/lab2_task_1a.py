"""
Task 1a: Ask  for  a  Fahrenheit degree from  the  
user,  then convert to  Celsius and  print the 
result as a float. 

• inputs : input = { x: x ∈ R and 200.0 ≥ x ≥ -100.0} 
• output : float (with epsilon = 1E-9) 
The output must be as follows: 
Enter Fahrenheit degree: 68 
20.0

(F = 1,8 C + 32)
"""

fah = float(input("Enter fahrenheit degree".ljust(25) + ":"))

print("Celsius value".ljust(25) + f": {((fah-32)/1.8):0.9f}")