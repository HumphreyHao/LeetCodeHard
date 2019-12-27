class Solution(object):
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            while nums[i]>0 and nums[i]<=len(nums) and nums[i]!=nums[nums[i]-1]:
                self.swap(nums,i,nums[i]-1)
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1
    def swap(self,nums,i,j):
        a = nums[i]
        nums[i]=nums[j]
        nums[j]=a
        
def main():
    solution = Solution()
    print(solution.firstMissingPositive([3,4,-1,1]))
main()