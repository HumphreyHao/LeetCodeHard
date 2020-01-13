from collections import deque
class Solution(object):
    def calculate(self, s:str):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        sign = 1
        num = 0
        stack =[]
        
        for c in s:
            if c.isdigit():
                #解决了连续数字的问题
                num = num*10+int(c)
            elif c == '+' or c == '-':
                res = res+num*sign
                sign =1 if c =='+' else -1
                num = 0
            elif c =='(':
                stack.append(res)
                stack.append(sign)
                sign =1 
                res =0
            elif c ==')':
                res = res + sign*num
                old_sign = stack.pop()
                old_res = stack.pop()
                res =old_res+old_sign*res
                sign =1
                num =0
        res = res+sign*num
        return res
                
        
            
            