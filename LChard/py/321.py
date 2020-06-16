def maxNumber(nums1, nums2, k):
    m=len(nums1)
    n=len(nums2)
    nums1.reverse()
    nums2.reverse()
    #初始化一个三维数组
    dp=[[[0]*k for j in range(n)] for i in range(m)]
    maxValue=0
    #因为i，j变化都要伴随着k变化，而单独k变化并不会影响值，所以无需初始化边
    j=0
    for i in range(1,m):
        for k1 in range(1,k):
            dp[i][j][k1]=10**(k1-1)*nums1[i]+dp[i-1][j][k1-1]
    i=0
    for j in range(1,n):
        for k1 in range(1,k):
            dp[i][j][k1]=10**(k1-1)*nums2[j]+dp[i][j-1][k1-1]
    k1=0
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j][k1]=dp[i-1][j-1][k1]
    for i in range(1,m):
        for j in range(1,n):
            for k1 in range(1,k):
                dp[i][j][k1]=max((10**(k1-1))*nums1[i]+dp[i-1][j][k1-1],(10**(k1-1))*nums2[j]+dp[i][j-1][k1-1],dp[i-1][j-1][k1])
                if dp[i][j][k1]>maxValue:
                    maxValue=dp[i][j][k1]
    result=str(maxValue).split()
    return result

maxNumber([3, 4, 6, 5],[9, 1, 2, 5, 8, 3],5)