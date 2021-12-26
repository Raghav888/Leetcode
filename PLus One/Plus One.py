
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        data=10**(len(digits)-1)
        data*=digits[0]
        for i in range(1,len(digits)):
            data+=digits[i]*(10**(len(digits)-(i+1)))
        data+=1
        return list(map(int,str(data)))
