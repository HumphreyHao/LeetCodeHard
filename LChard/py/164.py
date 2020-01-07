class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return 0
        min_val,max_val,n = float('inf'),float('-inf'),len(nums)
        for i in range(n):
            if nums[i]<min_val:
                min_val=nums[i]
            if nums[i]>max_val:
                max_val=nums[i]
        if min_val==max_val:
            return 0
        #用两个数组来代表桶，下标代表桶的index
        mins=[0]*(n+1)
        maxs=[0]*(n+1)
        has_num=[False]*(n+1)

        for num in nums:
            #使用比例确定当前数字存入哪个桶
            index=int((num-min_val) * n / (max_val-min_val))
            mins[index]=num if not has_num[index] else min(mins[index],num)
            maxs[index] = num if not has_num[index] else max(maxs[index], num)
            has_num[index] = True
        
        max_len=0
        m=maxs[0]
        for i in range(1,n+1):
            if has_num[i]:
                currLen = mins[i]-m
                if currLen>max_len:
                    max_len=currLen
                m=maxs[i]
        return max_len



        