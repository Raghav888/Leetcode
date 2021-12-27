class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(0,len(arr)-1):
            if arr[i]<arr[i+1]:
                great=i+1
        for i in range(0,len(arr)-1):
            if arr[i]>arr[i+1] :
                small=i
                break
        return small
        