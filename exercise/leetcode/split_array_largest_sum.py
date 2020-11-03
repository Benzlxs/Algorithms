"""
Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.
Write an algorithm to minimize the largest sum among these m subarrays.

Example 1
Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

"""

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        def check_if_this_sum_is_possible(sub_sum):
            number_of_splitting_points = 0
            current_subarray_sum = 0
            for num in nums:
                current_subarray_sum += num

                if current_subarray_sum > sub_sum:
                    number_of_splitting_points += 1
                    current_subarray_sum = num

                    if number_of_splitting_points > m - 1:
                        return False
            return True

        low_sum = max(nums)
        high_sum = sum(nums)

        while low_sum < high_sum:
            mid = low_sum + (high_sum - low_sum) // 2

            if check_if_this_sum_is_possible(mid):
                high_sum = mid
            else:
                low_sum = mid + 1
        return low_sum

