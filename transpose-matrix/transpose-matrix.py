class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        trans=[]
        for i in range(0,len(matrix[0])):
            trans.append([])
            for j in range(0,len(matrix)):
                trans[i].append(matrix[j][i])
        return trans
        