# =============================================================
# MATRIX INTERSECTION - FIND FIRST DUPLICATE CHALLENGE
# =============================================================

# Matrix containing lists of integers to be analyzed
integer_matrix = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


def find_first_duplicate(single_list):
    """
    Iterates through a list to find the first recurring integer.
    Uses a hash set for optimal O(n) time complexity.
    Returns the duplicate integer if found, otherwise returns -1.
    """
    seen_numbers = set()

    for number in single_list:
        if number in seen_numbers:
            return number
        seen_numbers.add(number)

    return -1


# =============================================================
# EXECUTION AND OUTPUT DISPLAY
# =============================================================
for sub_list in integer_matrix:
    result = find_first_duplicate(sub_list)
    print(f"For list {sub_list} -> The first duplicate is: {result}")