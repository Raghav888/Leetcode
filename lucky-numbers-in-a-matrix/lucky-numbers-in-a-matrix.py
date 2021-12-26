class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_data=[]
        for i in range(0,len(matrix)):
            min_data.append(min(matrix[i]))
        trans=[]
        for i in range(0,len(matrix[0])):
            trans.append([])
            for j in range(0,len(matrix)):
                trans[i].append(matrix[j][i])
        max_data=[]
        for i in range(0,len(trans)):
            max_data.append(max(trans[i]))
        for i in min_data:
            if i in max_data:
                return [i]