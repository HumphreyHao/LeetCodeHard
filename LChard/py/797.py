from typing import List
class Solution:
    def allPathsSourceTarget(self, graph):
        pashDict = {len(graph)-1:[[len(graph)-1]]}
        return self.dfs(0,graph,pashDict)

    def dfs(self,cur,graph,pashDict):
        if cur in pashDict:
            return pashDict[cur]
        res=[]
        for i in graph[cur]:
            res.extend(list(map(lambda x : [cur]+x,self.dfs(i,graph,pashDict))))
        pashDict[cur]=res
        return res

def main():
    sol = Solution()
    print(sol.allPathsSourceTarget([[1,2],[3],[3],[]]))
main()
    

        