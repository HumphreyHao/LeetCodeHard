class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        nextS='#'+("#").join(list(s))+"#"
        center=-1
        maxRight=-1
        p=[1]*len(nextS)
        for i in range(len(nextS)):
            if i >=maxRight:
                j=0
                while nextS[i+j]==nextS[i-j]:
                    j+=1
                    if i-j<0 or i+j>=len(nextS):
                        j-=1
                        break
                maxRight=i+j-1
                center=i
                p[i]=1+j
            else:
                p[i]=min(maxRight-i,p[2*center-i])
        res=0
        for i in range(len(p)):
            if i==p[i]-1:
                res=max(res,i)
        sC=s[res:]
        return sC[::-1]+s
def main():
    sol=Solution()
    print(sol.shortestPalindrome(
"aaaabbaa"))
main()
        
        
                
        