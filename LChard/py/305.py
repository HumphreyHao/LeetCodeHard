from typing import List
from collections import defaultdict
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        grid  = [[0]*n for _ in range(m)]
        island = defaultdict(set)
        
        directions =[[1,0],[-1,0],[0,-1],[0,1]]
        index =1
        res =[]
        
        for x,y in positions:
            if grid[x][y]:
                res.append(len(island))
                continue
            
            mark = []
            for dx,dy in directions:
                if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy] and grid[x+dx][y+dy] not in mark:
                    mark.append(grid[x+dx][y+dy])
            if len(mark) ==0:
                grid[x][y] =index
                island[index].add((x,y))
                index+=1
            else:
                temp = mark[0]
                grid[x][y] =temp
                island[temp].add((x,y))
                
                for num in mark[1:]:
                    for i,j in island[num]:
                        grid[i][j]=temp
                    island[temp] |=island[num]
                    del island[num]
            res.append(len(island))
        return res                    