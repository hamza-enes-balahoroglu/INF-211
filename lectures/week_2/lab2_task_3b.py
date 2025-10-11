"""
Task  3b:  Ask  for  an  input  string  from  the  user  and  print  the  string  with  only  letters  and 
numbers in the entered order. 
• Unwanted printable characters that should be removed are:   
!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ 
• Note that the string can include " or ' characters, so take necessary precautions.  
• inputs : input = {x: x ∈ printable characters except whitespaces and len(x)  ∈ [1, 100]}. 
• output : string 
The output must be as follows: 
Enter a string: :I!n#f21@1;,  
Inf211 
>>> 
Enter a string: :I!n'"#f"2%$/1@1;,.  
Inf211 

"""

text = input("Enter a text : ")
unwanted = {"!",'"',"#","$","%","&","\\","'"
            ,"(",")","*","+",",","-",".", "/", 
            ":", ";","<","=",">", "?","@","[","]",
            "^","`","{","|","}"}

if len(text) >= 1 and len(text)<=100:
    for i in unwanted:
        text = text.replace(i.strip(), '')
        pass
    pass

print(text)