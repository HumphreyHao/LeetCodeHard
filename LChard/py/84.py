from collections import deque
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights)==1:
            return heights[0]
        res=0
        stack =deque()
        stack.append(0)
        i=1
        while i<len(heights):
            if len(stack)==0 or heights[stack[-1]]<heights[i]:
                stack.append(i)
            else:
                tmpA=stack.pop()
                tmpB=stack[-1] if stack else -1
                res=max(res,heights[tmpA]*(i-tmpB-1))
                i-=1
            i+=1
        return res
                
                
        
def main():
    sol=Solution()
    print(sol.largestRectangleArea([1]))
main()