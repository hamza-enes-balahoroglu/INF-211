# Quiz 1

def T(r, c):
    if c == 1 and r >= 1:
        return 1
    if c == r and r >= 2:
        return T(r, c-1)
    if c>1 and r>c:
        return T(r, c-1) + T(r-1, c)
    pass

def F(r, c):
    if r < 1 or c < 1:
        return -0.5
    elif r == 1 and c >= 1:
        return 3
    elif c == r and r >= 2:
        return 2
    else:
        return F(r-1, c-1) + F(r, c-1)

    
x = int (input("X  : "))
result = 0

for i in range(1, x+1):
    k = ((-1)**i) * (i + 1)
    result += T(i+3, i) * F(k, i+2)
    pass

print(result)