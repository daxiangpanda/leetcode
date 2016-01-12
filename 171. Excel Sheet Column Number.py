#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for i in range(len(s)-1,-1,-1):
            num+=(ord(s[i])-ord('A')+1)*26**(len(s)-i-1)
        return num