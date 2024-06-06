#Sort a list without using the keyword sort: bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr



arr = [64, 34, 25, 12, 22, 11, 90]
# arr.sort()
# print(arr)
# print("sorted",sorted(arr))
print(bubble_sort(arr))