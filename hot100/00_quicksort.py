def partition(L,left,right):
    mid = L[left]
    while left < right:
        while left < right and L[right] >= mid:
            right -= 1
        L[left] = L[right]
        while left < right and L[left] <= mid:
            left += 1
        L[right] = L[left]
    L[left] = mid
    return left

def quicksort(L,start,end):
    if start < end:
        pviot = partition(L,start,end)

        quicksort(L,start,pviot-1)
        quicksort(L,pviot+1,start)

    return L


L = [5, 9, 1, 11, 6, 7, 2, 4]
start = 0
end = len(L) - 1
print(quicksort(L,start,end))

