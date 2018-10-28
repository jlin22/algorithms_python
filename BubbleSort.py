def sorted(array):
    """Returns a boolean of whether the array is sorted or not"""
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]: #array at next spot is greater 
            return False
    return True

def swap(array, p, q):
    temp = array[p]
    array[p] = array[q]
    array[q] = temp

def BubbleSort(array):
    """Uses bubble sort to return the sorted array"""
    for i in reversed(range(len(array))):
        #the array from i + 2 to the end is already sorted
        for j in range(i):
            if array[j] > array[j + 1]:
               swap(array, j, j + 1)
        #array[i + 1] (the end) is in the correct spot, along with i + 2 to the end
    assert(sorted(array))

unsorted = [4, 16, 124125, 6, 45, 1, 9]
sorted_array = [1, 5, 12, 21, 51, 65, 89, 120, 159, 189]
print(sorted(unsorted))
print(sorted(sorted_array))
BubbleSort(unsorted)
print(unsorted)


