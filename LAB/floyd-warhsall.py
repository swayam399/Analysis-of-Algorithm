def floyd_warshall(W,n):
    print(W[1][4])
    D=[]
    for i in range(1,n+1):
        row=[]
        for j in range(1,n+1):
            
            row.append(W[i][j])
            print(row)
        D.append(row)
        print(D)
        print("")
    for k in range(1,n):
        for i in range(1,n):
            for j in range(1,n):
                    print("i:",i)
                    print("j:",j)
                    print("k:",k)
                    if D[i][j] < D[i][k] + D[k][j]:
                        D[i][j] = D[i][k] + D[k][j]
    return D
INF = float('inf')
n = 4
W= [
    [INF,INF,INF,INF,INF],
    [INF,0,INF,3,INF],
    [INF,2,0,INF,INF],
    [INF,INF,7,0,1],
    [INF,6,INF,INF,0]
]
Shorted_path = floyd_warshall(W,n)
for i in range(1,n+1):
    for j in range(1,n+1):
        print(Shorted_path[i][j],end='\t')
    print()