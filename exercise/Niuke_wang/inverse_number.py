'''
Question:

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007

'''
import os
import fire
import time
import numpy as np
import time

class Solution:
    def InversePairs(self, data):
        # write code here
        if len(data) == 0:
             return 0

        def mergeSort(data, begin, end):
            if begin == end - 1:
                return 0
            mid = int((begin + end) / 2)
            left_count = mergeSort(data, begin, mid)
            right_count = mergeSort(data, mid, end)
            merge_count = merge(data, begin, mid, end)
            return left_count + right_count + merge_count

        def merge(data, begin, mid, end):
            i = begin
            j = mid
            count = 0
            temp = []
            while i < mid and j < end:
                if data[i] <= data[j]:
                    temp.append(data[i])
                    i += 1
                else:
                    temp.append(data[j])
                    j += 1
                    count += mid - i
            while i < mid:
                temp.append(data[i])
                i += 1
            while j < end:
                temp.append(data[j])
                j += 1
            data[begin: end] = temp
            del temp
            return count

        begin = 0
        end = len(data)
        ans = mergeSort(data, begin, end)
        return ans % 1000000007


def merge(left, right):
    # merging two parts
    sorted_list = []
    left_idx = right_idx = 0
    left_len, right_len = len(left), len(right)
    c = 0
    while (left_idx < left_len) and (right_idx < right_len):
        if left[left_idx] <= right[right_idx]:
            sorted_list.append(left[left_idx])
            left_idx += 1
        else:
            sorted_list.append(right[right_idx])
            right_idx += 1
            c += left_len - left_idx
    # merging together
    sorted_list = sorted_list + left[left_idx:] + right[right_idx:]
    return sorted_list, c

def merge_sort(list_nums):
    if len(list_nums) <= 1:
        return list_nums, 0
    mid = len(list_nums) // 2
    left, lc = merge_sort(list_nums[:mid])
    right, rc = merge_sort(list_nums[mid:])
    merge_list, mc = merge(left, right)
    return merge_list, (lc+rc+mc)



if __name__=='__main__':
    inputs = [1,2,3,4,5,6,7,0,2,90,10]
    number = 13
    s='googgle'
    t1 = time.time()
    input = 'aabc'
    #rs = jumpfloor(n)
    _, resut22=merge_sort(inputs)
    test = Solution()
    result = test.InversePairs(inputs)
    #rs = numberof1(-4)
    print("Time: {}, Results: {}".format(time.time()-t1, result))
    print("result2:{}".format(resut22))

