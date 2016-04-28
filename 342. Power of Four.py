class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        if num == 1:
            return True
        if num == 2:
            return False
        if bin(num-1)[2:].find('0') < 0 and (num-1)%3 == 0:
            return True
        else:
            return False

a = Solution()
for i in range(100):
    print a.isPowerOfFour(i)
