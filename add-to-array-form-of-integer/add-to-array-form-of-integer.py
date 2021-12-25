class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        base_value=10**(len(num)-1)
        base_value=base_value*num[0]
        for i in range(1,len(num)):
            base_value+=num[i]*(10**(len(num)-(1+i)))
        base_value+=k
        base_value=str(base_value)
        return list(map(int,base_value))
                            
