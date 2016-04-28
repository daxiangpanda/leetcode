class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<4:
            return n-1
        res = 1
        while n>2:
            res*=3
            n-=3
        if n==0:
            return res
        if n==1:
            return res/3*4
        if n==2:
            return res*2
a = Solution()
for i in range(3,10000):
    print str(i)+'  '+str(a.integerBreak(i))
