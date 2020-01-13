class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        rowMax=[0]*m
        lineMax=[0]*n
        for i in range(m):
            for j in range(n):
                tmp = grid[i][j]
                rowMax[i]=max(rowMax[i],tmp)
                lineMax[j]=max(lineMax[j],tmp)
        res=0
        for i in range(m):
            for j in range(n):
                res+=min(rowMax[i],lineMax[j])-grid[i][j]
        return res
    