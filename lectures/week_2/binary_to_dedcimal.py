# x = 0.652
# p = 0

# while ((2**p) % 1  != 0):
    
#     pass

print(int("1010", 2))

print(format(12, '016b'))

num = 102
binary = ''
while num > 0:
    binary = str(num % 2) + binary
    num //= 2
    print(binary)
    print(num)
    input()

print(binary)  # Output: 11001