class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #first to find the highest
        if len(height)==0:
            return 0
        maxIndex =0
        for i in range(len(height)):
            if height[i]>height[maxIndex]:
                maxIndex =i
        return self.findLeft(maxIndex,height)+self.findRight(maxIndex,height)
    def findLeft(self,maxIndex,height):
        if maxIndex ==0:
            return 0
        highest=0
        for i in range(maxIndex):
            if height[i]>height[highest]:
                highest= i
        return self.findLeft(highest,height)+self.helper(highest,maxIndex,height)
    def findRight(self,maxIndex,height):
        if maxIndex == len(height)-1:
            return 0
        highest =len(height)-1
        for i in range(maxIndex+1,len(height)):
            if height[i]>height[highest]:
                highest=i
        return self.findRight(highest,height)+self.helper(maxIndex,highest,height)
    def helper(self,left,right,height):
        sum=0
        for i in range(left+1,right):
            sum+=height[i]
        return min(height[left],height[right])*(right-left-1)-sum
def main():
    solution=Solution()
    print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
main()
            
        
        