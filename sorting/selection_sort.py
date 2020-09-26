# merge sortting https://en.wikipedia.org/wiki/Selection_sort
# time complexity is O(n^2)

import os
import time




def selection_sort(list_nums):
    for i in range(len(list_nums)):
        lowest_value_index = i
        # loop through unsorted times
        for j in range(i+1, len(list_nums)):
            if list_nums[j] < list_nums[lowest_value_index]:
                lowest_value_index = j

        list_nums[i], list_nums[lowest_value_index] = list_nums[lowest_value_index], list_nums[i]

    #return list_nums


if __name__=='__main__':
    # Verify it works
    random_list_of_nums = [120, 45, 68, 250, 176]

    print('Before sorting\n')
    print(random_list_of_nums)

    selection_sort(random_list_of_nums)

    print('After sorting\n')
    print(random_list_of_nums)

