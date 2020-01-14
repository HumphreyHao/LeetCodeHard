from collections import deque
class Solution:
    def alienOrder(self, words) -> str:
        nextMap = [[0]*26 for i in range(26)]
        indegree = [0]*26
        charSet =set()
        charSetAll = set()
        res=[]
        for i in range(len(words)-1):
            first = words[i]
            second = words[i+1]
            for i in range(min(len(first),len(second))):
                if first[i] == second[i]:
                    charSetAll.add(ord(first[i])-ord('a'))
                    continue
                else:
                    index1 = ord(first[i])-ord('a')
                    index2 = ord(second[i])-ord('a')
                    charSet.add(index1)
                    charSet.add(index2)
                    nextMap[index1][index2]=1
                    indegree[index2]+=1
                    break
        q =deque()
        for i in range(26):
            if i in charSet and indegree[i] ==0:
                q.append(i)
                break
        while q:
            i = q.popleft()
            res.append(chr(i+ord('a')))
            for j in range(26):
                if nextMap[i][j]==1:
                    indegree[j]-=1
                    if indegree[j]==0:
                        q.append(j)
        for i in charSetAll-charSet:
            res.append(chr(i+ord('a')))  
        return "".join(res)           
def main():
    sol = Solution()
    print(sol.alienOrder(['z','z']))
main()   
            
             