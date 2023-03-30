# comparison operators

a = 2
b = 3

print(a == b)  #equal to
print(a != b)  #not equal to
print(a>b)     #greater than
print(a >= b)  #greater than or equal to
print(a < b)   #less than
print(a <= b)  #less than or equal to

#logical operators

print((a == b) and (a!=b))
print((a <= b) or (a >b))
print(not (a >= b))

# bitwise operators
# declare binary variables
m = 0b01010011
n = 0b11111001

print(m)
print(n)
print(bin(m & n))  #binary
print(bin(m | n))
print(bin(m ^ n))
print(bin(~m))
print(bin(b << 3))
print(bin(b >> 2))