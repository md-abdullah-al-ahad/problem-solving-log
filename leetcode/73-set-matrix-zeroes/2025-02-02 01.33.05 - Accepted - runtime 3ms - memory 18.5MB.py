class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_idx = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range (0,m):
            for j in range (0,n):
                if matrix[i][j]==0:
                    zero_idx.append([i,j])
        for val in zero_idx:
            i = 0
            j = 0
            while i<m:
                matrix[i][val[1]]=0
                i+=1
            while j<n:
                matrix[val[0]][j]=0
                j+=1
        