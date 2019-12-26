from collections import deque
class Solution(object):
    def longestValidParentheses(self, s):
        res=0
        leftCount=0
        rightCount=0
        n=len(s)
        for i in s:
            if i=='(':
                leftCount+=1
            else:
                rightCount+=1
            if leftCount==rightCount:
                res=max(res,2*leftCount)
            elif rightCount>leftCount:
                rightCount=leftCount=0
        left=right=0
        for i in range(n-1,-1,-1):
            if s[i]=='(':
                leftCount+=1
            else:
                rightCount+=1
            if leftCount==rightCount:
                res=max(res,2*leftCount)
            elif leftCount>rightCount:
                rightCount=leftCount=0
        return res
    def longestValidParentheses1(self, s):
        res,start,n=0,0,len(s)
        st = deque()
        for i in range(n):
            if s[i]=='(':
                st.append(i)
            else:
                if len(st)==0:
                    start=i+1
                else:
                    st.pop()
                    res=max(res,i-start+1) if len(st)==0 else max(res,i-st[-1])
        return res
def main():
    solution=Solution()
    print(solution.longestValidParentheses1(")()())"))
main()