def quicksort(array):
    sort(array, 0, len(array) - 1)
    return array

def swap(array, p, q):
    """Swaps indices p and q of array"""
    temp = array[p]
    array[p] = array[q]
    array[q] = temp

def sort(array, low, high):
    """Sort the array from low to high inclusive"""
    if (low >= high):
        return
    pivot = array[high]
    i = low
    j = high
    while i < j:
        while array[i] < pivot and i < j:
            i += 1
        while array[j] >= pivot and i < j:
            j -= 1
        swap(array, i, j)
    swap(array, high, i)
    sort(array, low, i - 1)
    sort(array, i + 1, high)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
