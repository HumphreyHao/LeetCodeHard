class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        i =0
        n =len(intervals)
        #这一步是要找到插入位置，没有使用二分查找，可以优化
        while i<n and newInterval[0]>intervals[i][1]:
            i+=1
        left=i
        while i<n and newInterval[1]>=intervals[i][0]:
            i+=1
        right=i
        if left>=n:
            res=intervals+[newInterval]
        elif left==right:
            intervals.insert(left,newInterval)
            res=intervals
        else:
            res=intervals[:left]+[
                [min(intervals[left][0],newInterval[0]),max(intervals[right-1][1],newInterval[1])]
            ]+intervals[right:]
        return res
def main():
    sol=Solution()
    print(sol.insert([[1,5]],[0,3]))
main()
                
                
        
        
            