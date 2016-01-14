#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0
        for i in bin(n)[2:]:
            if i == '1':
                num+=1
        return num