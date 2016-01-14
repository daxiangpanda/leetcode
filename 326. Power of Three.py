#!/usr/bin/env python
# encoding: utf-8
# 1 数学知识很重要
# 2 round() 四舍五入 用法round(n,位数)
# 3 abs！！！
import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False
        if n==0:
            return False
        if abs(math.log(n)/math.log(3)-round(math.log(n)/math.log(3),0))<1e-10:
            return True
        else:
            return False

a = Solution()
print a.isPowerOfThree(19682)