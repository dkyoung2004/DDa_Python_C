N = int(input())
arr = list(map(int,input().split()))
sort_set = list(set(arr))

def quick_sort(array,start,end):
    if start >= end:
        return array
    pivot = start
    left = start+1
    right = end
    while(left<=right):
        while left <= end and arr[left] <= arr[pivot]:
            left += 1 

        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr, 0, right -1)
    quick_sort(arr, right + 1, end) 

quick_sort(sort_set, 0, len(sort_set)-1)
print(sort_set)
    