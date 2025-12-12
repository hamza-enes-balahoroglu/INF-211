def quiz2(text: str) -> str:
    result = ""
    for i in range(len(text)-1):
            
        if str(text[i+1]).isdecimal():
            result += text[i] * int(text[i+1])
            
        elif not str(text[i]).isdecimal():
            result += text[i]
    if not(str(text[-1]).isdecimal()):
        result += text[-1]

    return result

print(quiz2("a3ls3an2a"))