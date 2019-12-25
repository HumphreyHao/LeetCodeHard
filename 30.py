from collections import defaultdict
def findSubstring(s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(s) ==0 or len(words)==0:
            return []
        wordLength = len(words[0])
        winSize = len(words)*wordLength
        wordsSet=defaultdict(int)
        res=[]
        for word in words:
            wordsSet[word]+=1
        for i in range(wordLength):
            #for each position we need to traverse the whole str
            #first to get the init set of this loop
            left,right = i,i+winSize
            tmpSet=defaultdict(int)
            for j in range(left,right,wordLength):
                tmp =s[j:j+wordLength]
                tmpSet[tmp]+=1
            while right<=len(s):
                #比较两个字典是否完全相同
                if check(tmpSet,wordsSet):
                    res.append(left)
                if right+wordLength>len(s):
                    break
                tmpSet[s[left:left+wordLength]]-=1
                tmpSet[s[right:right+wordLength]]+=1
                left+=wordLength
                right+=wordLength
        return res
def check(tmpSet,wordsSet):
        for word in wordsSet:
            if word not in tmpSet:
                return False
            elif tmpSet[word] != wordsSet[word]:
                return False
        return True     
        
def main():
    print(findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"]));
main()
                