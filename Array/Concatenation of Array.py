
#Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length=len(nums)
        for i in range(0,length):
            nums.append(nums[i])
        return nums
