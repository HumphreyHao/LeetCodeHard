class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        #遍历数组找到所有的source点
        if len(ratings)==1:
            return 1
        dp=[1]*len(ratings)
        sources=[]
        for i in range(0,len(ratings)):
            if i ==0:
                if ratings[0]<=ratings[1]:
                    sources.append(0)
                    continue
            elif i ==len(ratings)-1:
                if ratings[i]<=ratings[i-1]:
                    sources.append(i)
                    continue
            elif ratings[i]<=ratings[i-1] and ratings[i]<=ratings[i+1]:
                sources.append(i)
        for source in sources:
            self.helperLeft(dp,source,ratings)
            self.helperRight(dp,source,ratings)
        return sum(dp)
    def helperLeft(self,dp,source,ratings):
        if source-1<0:
            return
        if ratings[source-1]<=ratings[source]:
            return
        dp[source-1]=max(dp[source]+1,dp[source-1])
        self.helperLeft(dp,source-1,ratings)
        return
    def helperRight(self,dp,source,ratings):
        if source+1>=len(ratings):
            return
        if ratings[source+1]<=ratings[source]:
            return
        dp[source+1]=max(dp[source]+1,dp[source+1])
        self.helperRight(dp,source+1,ratings)
        return
def main():
    sol=Solution()
    print(sol.candy([1,2,2]))
main()
    
           
        
        