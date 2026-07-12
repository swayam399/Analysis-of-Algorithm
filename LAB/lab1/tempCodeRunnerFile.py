def fibonacci(n):
    if n == 1:
        return 0;
    elif n == 2:
        return 1;
    else:
        a,b = 0,1
        for i in range(3,n+1):
            c = a +b;
            a=b
            b= c
        return c
print(fibonacci(0))