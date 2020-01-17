class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        m,n = len(image),len(image[0])
        up = binary_search(image, true, 0, x, 0, n, true)
        down = binary_search(image, true, x + 1, m, 0, n, false)
        left = binary_search(image, false, 0, y, up, down, true)
        right = binary_search(image, false, y + 1, n, up, down, false)
        return (right-left)*(down-up)
        def binary_search(image,h,i,j,low,high,opt):
            while i<j :
                k = low
                mid =(i+j)//2
                while k < high and (image[mid][k] if h else image[k][mid])=='0':
                    k+=1
                if k < high == opt:
                    j =mid
                else:
                    i =mid+1
            return i