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
    

def fibonacci(n):
    if n == 1:
        return 0;
    elif n == 2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
    
print(fibonacci(6))

# #HIGHEST FACTOR NIKALNEY TOTKA

def gcd_algorithm(a:int, b:int):
    if a == 0 and b==0:
        print("NO HCF")
    elif a ==0:
        return b
    elif b ==0:
        return a
    else:
        while b!=0:
            remainder = a%b;
            a = b
            b= remainder
    return a
print(gcd_algorithm(128,42))

def gcd_algorithm(a:int, b:int):
    if a == 0 and b==0:
        print("NO HCF")
    elif a ==0:
        return b
    elif b ==0:
        return a
    else:
        return gcd_algorithm(b,a%b)
print(gcd_algorithm(128,42))

#sequential search

def sequential(arr,elem):
    for i in range(len(arr)):
        if arr[i]==elem:
            
            return i
    return -1
result = sequential([1,2,3,4,5,6,7,8,9],1)
if result==-1:
    print("not found")
else:
    index = sequential
    print(f"found at index: {result}")