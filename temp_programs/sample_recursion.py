def factorial(n):
    if n==1:
        return n
    else:
        print(n)
        return   n * factorial(n-1)
 

print(factorial(4))