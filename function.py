def foo():
    print('foo()')
    
def calculate(a,b):
    val = a*b
    return val

def perform(num):
    d = num * 5
    return d, d + 5, d - 2

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
foo()
m = calculate(2,3)
print(m)

a,b,c = perform(5)
print(a)
print(b)
print(c)
res =fibonacci(10)
print(res)