#!/usr/bin/env python
# encoding: utf-8
class Solution:
    # @param n, an integer
    #  @return an integer
        def climbStairs(self, n):
            if n < 0:
                return -1
     # prevent invalid input: negative integer
            dp = [0,1,2]
            for i in range(3, n+1):
                dp.append(dp[i-1] + dp[i-2])
            return dp[n]