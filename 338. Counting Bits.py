#!/usr/bin/env python
# encoding: utf-8
# 算法挺好的 也不知道是怎么想出来的
class Solution(object):
    def countBits(self, num):
        lst = [0] * (num + 1)
        milestone = 0
        nextMilestone = 2
        for i in range(1, num + 1):
            if i == nextMilestone:
                milestone = nextMilestone
                nextMilestone = nextMilestone * 2
            # print milestone
            lst[i] = lst[i - milestone] + 1
            # print i
            # print lst
            # print bin(i)
        return lst

a = Solution()
a.countBits(100)