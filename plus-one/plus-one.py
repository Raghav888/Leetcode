class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ll=len(digits)
        data=10**(ll-1)
        data*=digits[0]
        for i in range(1,ll):
            data+=digits[i]*(10**(ll-(i+1)))
            print(data)
        data+=1
        return list(map(int,str(data)))