class Solution:
    def arrangeCoins(self, n: int) -> int:
        k=n
        i=1
        while (k!=0):
            k-=i
            i+=1
            if i>k:
                return i-1
            if i==k:
                return i
            
        