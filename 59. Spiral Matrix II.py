#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def gene(self,res,m):
        n = len(res)
        for i in range(m):
            res[(n-m)/2][(n-m)/2+i] = n**2-m**2+1+i
        for i in range(m):
            res[(n-m)/2+i][(n-m)/2+m-1] = n**2-m**2+1+m-1+i
        for i in range(m):
            res[(n-m)/2+m-1][(n-m)/2+m-1-i] = n**2-m**2+m-1+m+i
        for i in range(m-1):
            res[(n-m)/2+m-1-i][(n-m)/2] = n**2-m**2+1+3*m-3+i
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[1]*n for _ in xrange(n)]
        for i in range(n,0,-2):
            self.gene(res,i)
        return res
a = Solution()
res = [[11]*10 for _ in xrange(10)]
for i in a.generateMatrix(3):
    print i