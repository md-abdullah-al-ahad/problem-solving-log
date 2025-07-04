class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        hashset = {}
        row = len(mat)
        column = len(mat[0])
        rows = [0]*row
        columns = [0]*column
        for i in range (row):
            for j in range (column):
                hashset[mat[i][j]]=[i,j]
        for val in range (len(arr)):
            i = hashset[arr[val]][0]
            j = hashset[arr[val]][1]
            rows[i]+=1
            columns[j]+=1
            if rows[i]==column:
                return val
            if columns[j]==row:
                return val