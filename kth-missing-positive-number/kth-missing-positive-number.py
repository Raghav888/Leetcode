class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count=0
        for i in range(1,10000):
            if i not in arr:
                count+=1
                #print(count,arr[i-1])
                #print()
            if count==k:
                return i
            