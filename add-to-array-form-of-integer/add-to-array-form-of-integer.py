class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ll=len(num)
        base_value=10**(ll-1)
        base_value=base_value*num[0]
        for i in range(1,ll):
            new_val=num[i]*(10**(ll-(1+i)))
            base_value+=new_val
        base_value+=k
        base_value=str(base_value)
        return list(map(int,base_value))
                            