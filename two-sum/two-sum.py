class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new=[]
        
        for i in range(0,len(nums)):
            new.append((target-nums[i]))
        for i in range(0,len(nums)):
            if (new[i] in nums) and (i!=nums.index(new[i])):
                return [i,nums.index(new[i])]