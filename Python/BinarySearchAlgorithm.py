def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [2, 3, 5, 7, 11, 13]
target = int(input("Enter target number: "))
result = binary_search(arr, target)
print(f"Element found at index: {result}" if result != -1 else "Element not found")
