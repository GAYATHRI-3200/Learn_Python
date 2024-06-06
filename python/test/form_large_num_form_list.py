# Given array
# {54,546,548,60} -> 6054854654, 6054854654, 6054854654
# {1,34,3,98,9,76,45,4} ->998764543431, 998764543431

arr = [54,546,548,60]
# arr = [1, 34, 3, 98, 9, 76, 45, 4]

# Find the largest number
def sort_number(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            # print(arr[j] + arr[j+1], arr[j+1] + arr[j])
            if (arr[j] + arr[j+1] < arr[j+1] + arr[j]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
                yield arr
def largest_number(arr):
    arr = list(map(str,arr))
    print("arr",arr)
    large_num = sort_number(arr)
    for _ in large_num:
        pass
    return ''.join(arr)

largest_num = largest_number(arr)
print(largest_num)