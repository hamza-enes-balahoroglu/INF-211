"""
Task 1b: Ask for  a  Celsius degree  from  the  user, 
then convert to  Fahrenheit and  print the 
result as a float. 
• inputs : input = { x: x ∈ R and 100.0 ≥ x ≥ -100.0} 
• output : float (with epsilon = 1E-9) 
The output must be as follows: 
Enter Celsius degree: 20 
68.0 
 
"""


cel = float(input("Enter celsius degree".ljust(25) + ":"))

print("Fahrenheit value".ljust(25) + f": {(cel*1.8+32):0.9f}")