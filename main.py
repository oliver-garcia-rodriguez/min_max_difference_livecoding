def min_max_difference(the_array):

    the_highest_value = False
    the_smallest_number = False
    for i in the_array:

        if the_highest_value == False or the_smallest_number == False:
            the_highest_value = i
            the_smallest_number = i
        else:
            if the_highest_value < i:
                the_highest_value = i

            if the_smallest_number > i:
                the_smallest_number = i

    return the_highest_value - the_smallest_number

the_array = [15, 22, 84, 14, 88, 23]
the_difference = min_max_difference(the_array)
print(the_difference)