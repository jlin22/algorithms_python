def binary_search(input_array, value):
    """Given a sorted array, find the index of the value. If it is not in the
    array, return -1"""
    """Remember to include the bottom and exclude the top. Allow for low ==
    high. Boundaries are not necessary, but are useful for the first try"""
    low = 0 
    high = len(input_array)
    while low <= high: #and low >= 0 and high <= len(input_array):
        mid = (low + high) // 2
        print("{} {} {}".format(low, mid, high))
        if input_array[mid] < value:
            low = mid + 1
        elif input_array[mid] > value:
            high = mid - 1
        else:
            return mid
    return -1

test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
print(binary_search(test_list, 29))
print(binary_search(test_list, 1))
