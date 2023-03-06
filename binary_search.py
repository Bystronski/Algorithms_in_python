def binary_search(number_list, search_number):
    low = 0
    high = len(number_list) - 1

    while low <= high:
        middle = (low + high)
        search = number_list[middle]
        if search == search_number:
            return middle
        if search > search_number:
            high = middle - 1
        else:
            low = middle + 1
    return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))  # => 1
print(binary_search(my_list, -1))  # => None
