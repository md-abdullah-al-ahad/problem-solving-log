class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        lst = [0]*(n*n)
        z = 0
        for i in range (n):
            for j in range (n):
                lst[z]=matrix[i][j]
                z+=1
        j = n - 1
        k = 0
        for j in range (n-1,-1,-1):
            i = 0
            while i<n:
                matrix[i][j]=lst[k]
                i+=1
                k+=1