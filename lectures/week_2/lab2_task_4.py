"""
Task  4:  Ask  for  an  input  from  the  user  containing  only  parentheses.  Then  print  if  the 
parentheses are actually in correct order (or it is valid). 
• The parentheses are valid if  open brackets closed by the  same type of  brackets and 
open brackets closed in the correct order. 
• inputs: input = {x: x ∈ "{,},(,),[,]" and len(x) ∈ [1, 100]} 

The output must be as follows: 
>>> 
Enter input: {}  
True 
>>> 
Enter input: {}{}[]  
True 
>>> 
Enter input: {([])}[]  
True 
>>> 
Enter input: {(})  
False 
Explanation: After {( expression, first ( should be closed with ), 
then }. 
>>> 
Enter input: [()  
False
"""

girdi = input("Parantezli ifade girin :")

hafiza = ""

sonuc = True

for i in girdi:
    if i in "({[":
        hafiza += i
        pass
    elif i in ")}]":
        if hafiza != "":
            
            if i==")" and hafiza[-1] == "(":
                hafiza = hafiza[0:-1]
                pass
            elif i=="]" and hafiza[-1] == "[":
                hafiza = hafiza[0:-1]
                pass
            elif i=="}" and hafiza[-1] == "{":
                hafiza = hafiza[0:-1]
                pass
            else:
                valid = False
            break
        pass
    pass

if hafiza != "":
    sonuc = False
    pass

print(sonuc)