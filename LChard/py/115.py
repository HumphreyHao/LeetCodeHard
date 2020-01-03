class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ls = len(s)
        lt = len(t)
        if ls < lt:
            return 0
        dp = [[0 for _ in range(ls)] for _ in range(lt)]
        for i in range(lt):
            for j in range(i, ls):
                if t[i] == s[j]:
                    if i == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = sum(dp[i - 1][:j])
        return sum(dp[-1])