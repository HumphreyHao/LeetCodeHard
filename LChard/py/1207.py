from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        wordDict=defaultdict(int)
        for i in arr:
            wordDict[i]+=1
        wordSet=set()
        for i in wordDict:
            if wordDict[i] not in wordSet:
                wordSet.add(wordDict)
            else:
                return False
        return True
            