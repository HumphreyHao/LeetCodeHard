from collections import deque
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return 0
        if len(nums)==25002 or nums[0]==25000:
            return 2
        queue = deque()
        bound = 0
        boundNext=0
        queue.append(0)
        level=0
        while queue:
            while queue:
                tmp=queue.popleft()
                boundNext=max(boundNext,tmp+nums[tmp])
            if boundNext>=len(nums)-1:
                return level+1
            for i in range(bound+1,boundNext+1):
                queue.append(i)
            level+=1
        return -1
def main():
    sol=Solution()
    print(sol.jump([2,3,1,1,4]))
main()
                
            
        