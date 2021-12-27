class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c=0
        for i in grid:
            for g in i:
                if(g<0):
                    c+=1
        return c
        