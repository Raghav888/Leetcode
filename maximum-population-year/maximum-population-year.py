class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        arr=[0]*101
        for x,y in logs:
            for i in range(x,y):
                arr[i-1950]+=1
        return (1950+arr.index(max(arr)))
        