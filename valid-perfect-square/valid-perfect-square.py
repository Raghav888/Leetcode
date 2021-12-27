class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1: return True
        i=1
        result=1
        while(result<=num):
            i+=1
            result=i*i
        i-=1
        if(num==(i*i)):
            return True
        return False