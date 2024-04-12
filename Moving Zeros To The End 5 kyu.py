def move_zeros(lst):
    zeros = []
    non_zeros = []
    for element in lst:
        if element == 0:
            zeros.append(element)
        else:
            non_zeros.append(element)
    return non_zeros + zeros