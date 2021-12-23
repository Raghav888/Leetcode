#Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

#Return the array in the form [x1,y1,x2,y2,...,xn,yn]

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
    
        for i in range(0,n):
            nums.append(nums[i])
            nums.append(nums[i+n])
        for i in range(0,2*n):
            nums.pop(0)
        return nums
