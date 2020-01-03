from collections import defaultdict
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        countSet=defaultdict(int)
        length=0
        for i in nums:
            countSet[i]=0
        
        for i in nums:
            if countSet[i]==1:
                continue
            else:
                left=self.findLeft(countSet,i)
                right = self.findRight(countSet,i)
                length=max(length,left+right+1)
        return length
    
    def findLeft(self,countSet,i):
        if i-1 in countSet:
            countSet[i-1]=1
            return self.findLeft(countSet,i-1)+1
        else:
            return 0
    def findRight(self,countSet,i):
        if i+1 in countSet:
            countSet[i+1]=1
            return self.findRight(countSet,i+1)+1
        return 0
def main():
    sol=Solution()
    print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
main()
                
                
            
        
            
        