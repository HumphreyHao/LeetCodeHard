class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        #count how many nodes
        count =0
        tmp=head
        while tmp!=None:
            tmp =tmp.next
            count+=1
        if count<k:
            return head
        pre =None
        current =head
        count=0
        while current!=None:
            next =current.next
            current.next=pre
            pre=current
            current=next
            count+=1
            if count ==k:
                break
        if current ==None:
            return pre
        else:
            head.next =self.reverseKGroup(self,current,k)
            return pre
        
            
