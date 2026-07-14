def floyd_warshall(W, n):
    D = []
    for i in range(1, n+1):
        row = []
        for j in range(1, n+1):
            row.append(W[i][j])
        D.append(row)

    # Floyd-Warshall algorithm
    for k in range(n):         
        for i in range(n):     
            for j in range(n):
        
                if D[i][k] != INF and D[k][j] != INF:
            
                    if D[i][j] > D[i][k] + D[k][j]:
                        D[i][j] = D[i][k] + D[k][j]
    return D

INF = float('inf')
n   = 3
W = [
     [INF, INF, INF, INF],   # dummy row 0
    [INF,   0,   4,   7],   # node 1
    [INF,   1,   0,   2],   # node 2
    [INF,   6, INF,   0] 
]

Shortest_path = floyd_warshall(W, n)

# ✅ Print correctly using 0-indexed
print("\nShortest Path Matrix:")
print("     1\t  2\t  3\t  4")
for i in range(n):
    print(f"{i+1}", end="  ")
    for j in range(n):
        val = Shortest_path[i][j]
        print("INF" if val == INF else val, end="\t")
    print()