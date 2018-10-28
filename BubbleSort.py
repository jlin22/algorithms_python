def BubbleSort(array):
    """Uses bubble sort to return the sorted array"""

def sorted(array):
    """Returns a boolean of whether the array is sorted or not"""
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]: #array at next spot is greater 
            return False
    return True

unsorted = [4, 16, 124125, 6, 45, 1, 9]
sorted_array = [1, 5, 12, 21, 51, 65, 89, 120, 159, 189]
print(sorted(unsorted))
print(sorted(sorted_array))

