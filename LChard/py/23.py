import heapq
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        minHeap =[]
        heapq.heapify(minHeap)
        for head in lists:
            if head!=None:
                heapq.heappush(minHeap, [head.val,head])
        pre = ListNode(0)
        res=pre
        while minHeap:
            pre.next = heapq.heappop(minHeap)[1]
            if pre.next.next!=None:
                heapq.heappush(minHeap,[pre.next.next.val,pre.next.next])
            pre= pre.next
        return res.next
                
            
        
        