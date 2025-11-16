# Quiz 2

def is_polindrom(text):
    
    if len(text) <= 3 and text[0] == text[-1]:
        return True
        
    if text[0] == text[-1]:
        return is_polindrom(text[1:-1])
    
    return False

text = input("Enter a text : ")

print(is_polindrom(text))