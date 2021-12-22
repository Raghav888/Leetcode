#Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        length=len(nums)
        for i in range(0,length):
            nums.append(nums[nums[i]])
        for i in range(0,length):
            nums.pop(0)
          
        return nums
