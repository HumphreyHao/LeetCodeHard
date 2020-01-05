class Solution:
    def wordBreak(self, s: str, wordDict: list) -> list:
        if not s:
            return []
        _len,wordDict=len(s),set(wordDict)
        _min,_max=2147483647,-2147483648
        for word in wordDict:
            #这两步是要找到最小单词长度，从而减少不必要的遍历
            _min=min(_min,len(word))
            _max=max(_max,len(word))
    
        def dfs(start):
            if start not in memo:
                res=[]
                for i in range(_min,min(_max,_len-start)+1):
                    if s[start:start+i] in wordDict:
                        res.extend(list(map(lambda x : s[start:start+i]+" "+x,dfs(start+i))))
                memo[start]=res
            return memo[start]

        memo={_len:[""]}
        return list(map(lambda x:x[:-1],dfs[0]))
        