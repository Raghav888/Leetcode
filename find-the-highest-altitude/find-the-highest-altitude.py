class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum_data=0
        length=len(gain)
        gain.append(0)
        for i in range(0,length):
            sum_data+=gain[i]
            gain.append(sum_data)
        for i in range(0,length):
            gain.pop(0)
        return max(gain)
            
            
            
        