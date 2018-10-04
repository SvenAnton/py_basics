"""Adding."""


def get_max_element(int_list):
    """
    Return the maximum element in the list.

    If the list is empty return None.
    :param int_list: List of integers
    :return: largest int
    """
    return max(int_list)


def get_min_element(int_list):
    """
    Return the minimum element in list.

    If the list is empty return None.
    :param int_list: List of integers
    :return: Smallest int
    """
    return min(int_list)


def sort_list(int_list):
    """
    Sort the list in descending order.

    :param int_list: List of integers
    :return: Sorted list of integers
    """
    int_list.sort(reverse = True)
    return int_list


def add_list_elements(int_list):
    """
    Create a new sorted list of the sums of minimum and maximum elements.

    Add together the minimum and maximum element of int_list and add that sum to a new list
    Repeat the process until all elements in the list are used, ignore the median number
    if the list contains uneven amount of elements.
    Sort the new list in descending order.
    This function must use get_min_element(), get_max_element() and sort_list() functions.
    :param int_list: List of integers
    :return: Integer list of sums sorted in descending order.
    """
    iterations = len(int_list) // 2
    new_list = []

    for i in range(iterations):
        sum = get_max_element(int_list) + get_min_element(int_list)
        new_list.append(sum)
        int_list.remove(get_max_element(int_list))
        int_list.remove(get_min_element(int_list))
    return sort_list(new_list)
