from collections import deque,defaultdict
class Word:
    def __init__(self,string,path):
        self.str=string
        self.path=path
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordDict=defaultdict(set)
        res=[]
        for word in wordList:
            wordDict[word]=set()
        queue = deque()
        letters="qwertyuioplkjhgfdsazxcvbnm"
        #queue 里要存一个对象，需要把它的当前路径也带上去
        begin=Word(beginWord,[beginWord])
        queue.append(begin)
        flag=0
        while queue:
            count =len(queue)
            while count>0:
                tmp = queue.popleft()
                tmpStr  = tmp.str
                tmpPath = tmp.path
                if len(wordDict[tmpStr])!=0:
                    for nextStr in wordDict[tmpStr]:
                        if nextStr==tmpStr:
                            continue
                        if nextStr==endWord:
                            flag =1
                        if nextStr in wordDict and nextStr not in tmpPath:
                            nextPath = list(tmpPath)
                            nextPath.append(nextStr)
                            queue.append(Word(nextStr,nextPath))
                            if nextStr==endWord:
                                res.append(nextPath)
                #生成字典中的每一个字符串变换一个字符能到达的字符串计算了多次，可以用list化简
                else:
                    for i in range(0,len(tmpStr)):
                        for letter in letters:
                            nextStr = tmpStr[0:i]+letter+tmpStr[i+1:]
                            if nextStr==tmpStr:
                                continue
                            if nextStr==endWord:
                                flag =1
                            if nextStr in wordDict and nextStr not in tmpPath:
                                wordDict[tmpStr].add(nextStr)
                                nextPath = list(tmpPath)
                                nextPath.append(nextStr)
                                queue.append(Word(nextStr,nextPath))
                                if nextStr==endWord:
                                    res.append(nextPath)
                count-=1
            if flag ==1:
                break
        return res
def main():
    sol = Solution()
    print(sol.findLadders("hit","cog",["hot","dot","dog","lot","log","cog"]))
main()
            
            
        
        
    
    