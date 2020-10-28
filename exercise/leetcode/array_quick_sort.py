Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.




class Solution:
    # use the indice of array to sort
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            # save each nums[i] to the position i = nums[i] - 1
            while nums[nums[i] - 1] != nums[i]:
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp

            # if nums[i] already there, return nums[i]
            if nums[i] - 1 != i and nums[nums[i] - 1] == nums[i]:
                return nums[i]


