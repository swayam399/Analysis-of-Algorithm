def find(parent,i):
    while parent[i]!=i:
        i = parent[i]
    return i
def union(parent,x,y):
    parent[find(parent,x)] = find(parent,y)
def krushkal_algorithm(vertex,edge):
    parent = [i for i in range(vertex)]
    total_cost = 0
    mst = []
    for x,y,w in edge:
        if find(parent,x)!=find(parent,y):
            mst.append((x,y,w))
            total_cost+=w
            union(parent,x,y)
    return mst,total_cost
vertex = 4
edge = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]
mst,total_cost = krushkal_algorithm(vertex,edge)
for x,y,w in mst:
     print(f"{x} - {y} : {w}")

print("Total Cost =", total_cost)