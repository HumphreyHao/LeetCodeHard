import heapq
class MedianFinder(object):
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        #最大堆
        self.small =[]
        #总是使得最大堆的长度《=最小堆堆长度+1
        #最小堆
        self.big   =[]
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.big,num)
        self.balance(self.small,self.big)
        
    def balance(self,small,big):
        if (len(small)+len(big))%2 ==1:
            while len(small)<len(big)+1:
                heapq.heappush(small,-heapq.heappop(big))
        else:
            while len(small)!=len(big):
                heapq.heappush(small,-heapq.heappop(big))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) == len(self.big):
            return float((-self.small[0]+self.big[0])/2)
        else :
            return -self.small[0]
def main():
    sol = MedianFinder()
    sol.findMedian()
    sol.addNum(1)
    sol.addNum(2)
    print(sol.findMedian())
main()