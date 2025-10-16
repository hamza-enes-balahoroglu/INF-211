# 2. Quiz

text = input("Enter A text : ")
counter = 0
result = 0
for i in text:
    if i.isdecimal():
        if counter % 2 ==0:
            result += int(i)
        else:
            result -= int(i)
        counter += 1
        pass
    pass

print(result)