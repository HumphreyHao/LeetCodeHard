def KMP(mom,son):
    next=[-1]*len(son)
    getNext(next,son)
    m=s=0
    #初始指针初始化为0
    while (s<len(son) and m < len(mom)):
        if mom[m] == son[s]:
            m+=1
            s+=1
        else:
            s= next[s]
    
    if s == len(son):
        return m-s
    
    return -1

def getNext(next,son):
    #'ABCDABD'
    if len(son)>1:
        next[1]=0
        i,j=1,0
        #这里要解释一下，i代表的是后缀的末尾，j代表的是前缀的末尾，相当于是两个P在匹配，j代表的P在移动
        while i < len(son)-1:
            if j==-1 or son[i]==son[j]:
                i+=1
                j+=1
                next[i]=j
            else:
                j=next[j]
        
    