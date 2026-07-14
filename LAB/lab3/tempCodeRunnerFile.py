def merge_sort(A,l,r):
    if l<r:
        m = int((l+r)/2)
        merge_sort(A,l,m)
        merge_sort(A,m+1,r)
        merge(A,l,m+1,r)
    return A
def merge(A,l,m,r):
    i  = l
    j = r
    k = m
    B = []
    while (i<m and k<=j ):
        if (A[i]<A[k]):
            B.append(A[i])
            i+=1
        else:
            B.append(A[k])        
            k+=1
    while (i < m):
        B.append(A[i]) 
        i+=1
    while (k<=j):
        B.append(A[k])    
        k+=1
    for index in range(len(B)):
        A[l+index] = B[index]
    return A
A=[1,2,3,4,5,623,22,234,5532,2,43]
print("Before merge_sort: ", A)
sorted = merge_sort(A,0,len(A)-1)
print("After merge_sort: ", sorted)