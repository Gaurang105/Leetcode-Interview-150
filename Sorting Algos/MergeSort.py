from typing import List

def mergeSort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

input_str = input('Enter elements of array separated by space:\n')
arr = [int(num) for num in input_str.split(' ')]
sorted_arr = mergeSort(arr)
print(sorted_arr)