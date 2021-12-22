#Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        length=len(nums)
        sum_array=0
        ans=[]
        for i in range(0,length):
            sum_array+=nums[i]
            ans.append(sum_array)
        return ans
        
