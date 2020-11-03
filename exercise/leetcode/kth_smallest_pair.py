"""
Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.

Example 1
Input:
nums = [1,3,1]
k = 1
Output: 0
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.

"""

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # nlogn
        nums.sort()
        ans = 0
        l, r = 0, max(nums) - min(nums)
        # nlogn
        while l <= r:
            mid = (l+r) // 2
            count = self.helper(mid, nums)
            if count >= k:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

    def helper(self, mid, nums):
        count = 0
        i = 0
        j = 1
        while i < len(nums):
            j = max(j, i+1)
            while j < len(nums) and nums[j] - nums[i] <= mid:
                j += 1
            count += j - 1 - i
            i += 1
        return count

