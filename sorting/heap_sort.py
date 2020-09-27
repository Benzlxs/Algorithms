# heap sortting https://en.wikipedia.org/wiki/Heapsort
# time complexity is O(nlog(n)).

import os
import time



def heapify(nums, heap_size, root_index):
    # Assume the index of the largest element is the root index
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # If the left child of the root is a valid index, and the element is greater
    # than the current largest element, then update the largest element
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # Do the same for the right child of the root
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # If the largest element is no longer the root element, swap them
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(nums, heap_size, largest)


def heap_sort(list_nums):
    n = len(list_nums)

    # travese each node, sortting each local binary tree
    for i in range(n,-1,-1):
        heapify(list_nums, n, i)

    # Move the root of the max heap to the end, and start to swap each node
    for i in range(n - 1, 0, -1):
        list_nums[i], list_nums[0] = list_nums[0], list_nums[i]
        heapify(list_nums, i, 0)


if __name__=='__main__':
    # Verify it works
    random_list_of_nums = [120, 45, 68, 250, 176]

    print('Before sorting\n')
    print(random_list_of_nums)

    heap_sort(random_list_of_nums)

    print('After sorting\n')
    print(random_list_of_nums)

