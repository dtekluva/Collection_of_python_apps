def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1,101):
    print(n,':',fibonacci(n))

##fibonacci_cache = {}
##
##def fibonacci(n):
#### If we have cached the value, then return it
##    if n fibonacci_cache:
##        return fibonacci_cache[n]
##
#### Compute the Nth term
##    if 
