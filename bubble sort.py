# Program to sort the elements of an array using bubble sort.

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Last i elements are already in place, so no need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

my_array = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_array)

print("Sorted array is:")
print(my_array)