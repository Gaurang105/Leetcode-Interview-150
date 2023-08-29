from typing import List

def selectionSort(arr: List[int]) -> None: 
    n = len(arr)

    for i in range(n):
        mini = arr[i]
        minIndex = i

        for j in range(i, n):
            if arr[j] < mini:
                mini = arr[j]
                minIndex = j

        arr[i], arr[minIndex] = arr[minIndex], arr[i]

        
