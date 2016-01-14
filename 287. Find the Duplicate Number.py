#!/usr/bin/env python
# encoding: utf-8
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)-1
        dict = {}
        for i in range(1,n+1):
            dict[i] = 0
        # print dict
        for i in nums:
            if dict[i] == 1:
                return i
            dict[i]+=1
a = Solution()
nums = [1,1]
print a.findDuplicate(nums)