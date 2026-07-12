def greedy_knapsack(X,V,W,M):
    n = len(X)
    items=[]
    for i in range(n):
        ratio = V[i]/W[i]
        items.append((ratio,X[i],V[i],W[i]))
        
    items.sort(reverse=True)
    S = []
    SW=0
    SP=0
    i=0
    
    while i<n:
        ratio,X,P,W=items[i]
        if(SW+W)<=M:
            S.append(X)
            SW = SW+W
            SP = SP+ P
        else:
            F = (M-SW)/W
            S.append((X,F))
            SW = SW+W*F
            SP = SP+P*F
            break
        i = i+1
    return S,SW,SP

X=['x1','x2','x3','x4','x5','x6','x7']
M=28
P=[9,5,2,7,6,16,3]
W= [2,5,6,11,1,9,1]
S,SW,SP = greedy_knapsack(X,P,W,M)
print(f"s is:", S)
print(f"sw is:", SP)
print(f"sp is:", SW)

   

