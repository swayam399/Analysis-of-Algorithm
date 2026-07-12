def quick_sort(A,low,high):
    if low<high:
        p = partition(A,low,high)
        quick_sort(A,low,p-1)
        quick_sort(A,p+1, high)
def partition(A,low,high):
    pivot = A[low]
    x= low+1
    y = high
    while x<=y:
        while A[x]<=pivot and x<=high:
            x = x+1
        while y>low+1 and A[y]>=pivot:
            y=y-1
        if x<y:


            A[x],A[y]=A[y],A[x]
    A[low],A[y] = A[y],A[low] 

    return y
arr=[44,22,33,77,11,55,66]
print("Original array: ",arr)
quick_sort(arr,0,len(arr)-1)
print("Sorted ARRAy: ",arr)