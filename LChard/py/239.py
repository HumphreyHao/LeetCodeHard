from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums)==0:
            return 0
        q=deque()
        res=[]
        if k ==1:
            return nums
        q.append(nums[0])
        for i in range(1,k):
            tmp = nums[i]
            while q and tmp > q[-1]:
                q.pop()
            q.append(tmp)
        res.append(q[0])
        for i in range(k,len(nums)):
            j=i-k
            left = nums[j]
            right= nums[i]
            if left == q[0]:
                q.popleft()
            while q and right>q[-1]:
                q.pop()
            q.append(right)
            res.append(q[0])
        return res
def main():
    sol = Solution()
    print(sol.maxSlidingWindow([-7,-8,7,5,7,1,6,0],4))
main()
        
        
                    
                
            