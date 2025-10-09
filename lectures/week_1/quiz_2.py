my_name = "Hamza"


f = int(input("First Num  : "))
s = int(input("Second Num : "))

result = ""

for i in range(0, len(my_name)):
    if i >= f and i <= s:
        continue
    result += my_name[i]
    pass

print(result)
