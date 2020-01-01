from collections import defaultdict
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left,right=0,0
        tDict =defaultdict(int)
        wDict =defaultdict(int)
        res=[-1,-1]
        for i in t:
            tDict[i]+=1
        #stage 1: only right
        while right<len(s):
            rightA=s[right]
            if rightA in tDict:
                wDict[rightA]+=1
                if self.check(tDict,wDict):
                    break
            right+=1
        if right==len(s):
            return ""
        #stage 2:only left
        while left<right:
            leftA=s[left]
            if leftA in tDict:
                if wDict[leftA]-1<tDict[leftA]:
                    break
                wDict[leftA]-=1
            left+=1
        res[0],res[1]=left,right
        #stage 3:move together
        while right<len(s)-1:
            wDict[s[left]]-=1
            left+=1
            right+=1
            wDict[s[right]]+=1
            leftA=s[left]
            rightA=s[right]
            if self.check(tDict,wDict):
                while left<right:
                    if s[left] in tDict:
                        if wDict[s[left]]-1<tDict[s[left]]:
                            break
                        wDict[s[left]]-=1
                    left+=1
                if right-left < res[1]-res[0]:
                    res[1],res[0]=right,left
        if left==-1:
            return ""
        return s[res[0]:res[1]+1]
            
            
    def check(self,tDict,wDict):
        for i in tDict:
            if i not in wDict:
                return False
            elif wDict[i]<tDict[i]:
                return False
        return True
def main():
    sol=Solution()
    print(sol.minWindow("a","aa"))
main()
        