class Solution:
    def strobogrammaticInRange(self, low, high):
        len1, len2 = len(low), len(high)
        result = 0
        if len1 == len2:
            temp = self.findStrobogrammatic(len1)
        else:
            for i in range(len1 + 1, len2):
                result += self.process1(i)
            if low == "9" * len1:
                temp1 = []
            else:
                temp1 = self.findStrobogrammatic(len1)
            if high[0] == "1" and high[1:] == "0" * (len2 - 1):
                temp2 = []
            else:
                temp2 = self.findStrobogrammatic(len2)
            temp = temp1 + temp2
        index = 0
        while index < len(temp):
            if int(low) <= temp[index] <= int(high):
                result += 1
            index += 1
        return result

    def findStrobogrammatic(self, n):
        nums = ["0", "1", "6", "8", "9", "6", "8", "9", "1", "0"]
        result = []
        self.process(nums, "", "", n, result)
        result = list(map(int, result))
        result = list(map(str, result))
        index = 0
        while index < len(result):
            if len(result[index]) < n:
                result.remove(result[index])
            else:
                break
        result = list(map(int, result))
        return result

    def process(self, nums, temp1, temp2, n, result):
        if n == 0:
            result.append(temp1 + temp2)
        elif n == 1:
            result.append(temp1 + "0" + temp2)
            result.append(temp1 + "1" + temp2)
            result.append(temp1 + "8" + temp2)
        else:
            size = len(nums)
            for i in range(size // 2):
                self.process(nums, temp1 + nums[i], nums[size - 1 - i] + temp2, n - 2, result)

    def process1(self, n):
        if n == 1:
            return 5
        result = [4]
        self.process2(n - 2, result)
        return result[0]

    def process2(self, n, result):
        if n == 0:
            return
        if n == 1:
            result[0] *= 3
            return
        else:
            result[0] *= 5
            self.process2(n - 2, result)