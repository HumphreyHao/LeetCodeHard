class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie={}
        for word in words:
            node = trie
            for char in word:
                #这个函数的意思是插入这个值，并且返回值；如果key不存在，就插入；如果已经存在就返回
                node = node.setdefault(char,{})
            #这里是标志这个节点是末尾节点
            node['#']=True
        
        def search(i,j,node,pre,visited):
            if '#' in node:
                res.add(pre)
            for (di,dj) in ((-1,0),(1,0),(0,-1),(0,1)):
                ii=i+di
                jj=j+dj
                if -1<ii<h and -1<jj<w and board[ii][jj] in node and (ii,jj) not in visited:
                    search(ii,jj,node[board[ii][[jj]]],pre+board[ii][jj],visited | {(ii,jj)})
        res, h, w = set(),len(board),len(board[0])
        for i in range(h):
            for i in range(w):
                if board[i][j] in trie:
                    search(i,j,trie[board[i][j]],board[i][j],{(i,j)})
        return list(res)
                

        