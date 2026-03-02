def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Flag to check if swapping happens
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
