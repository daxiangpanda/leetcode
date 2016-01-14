#!/usr/bin/env python
# encoding: utf-8
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = []
        while True:
            res = 0

            for i in str(n):
                res+=int(i)**2
            if res in result:

                return False

            result.append(res)
            # print res
            n = res
            if n == 1:
                return True
a = Solution()
for i in range(100):
    # print i
    print str(i)+':'+str(a.isHappy(i))
