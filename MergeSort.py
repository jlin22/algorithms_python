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

def merge(array, aux, low, mid, high):
    """Merges low->mid, (mid+1)->high"""
    #create i (tracker for array low->mid), j (tracker for array (mid+1)->high)
    i = low
    j = mid + 1
    #create k (tracker for auxiliary array)
    k = low
    while k <= high:
        if i > mid: #first array is done
            aux[k] = array[j]
            j += 1
        elif j > high: #second array is done
            aux[k] = array[i]
            i += 1
        elif array[i] > array[j]:
            aux[k] = array[j]
            j += 1
        else:
            aux[k] = array[i]
            i += 1
        k += 1
    #copy the values for subarray low->high into the original array
    for x in range(low, high + 1):
        array[x] = aux[x]

def sort(array, aux, low, high):
    if high <= low:
        return
    mid = (high + low) // 2
    sort(array, aux, low, mid)
    sort(array, aux, mid + 1, high)
    merge(array, aux, low, mid, high)

def MergeSort(array):
    aux = array.copy()
    sort(array, aux, 0, len(array) - 1)

unsorted = [1, 6, 124, 54, 12, 67, 43, 23, 12]
a = [1, 6, 3, 4]
aux = a.copy()
merge(a, aux, 0, 1, 3)
print(a)

#MergeSort(unsorted)
