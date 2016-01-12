#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for i in set(nums):
            dict[i] = 0
        for i in nums:
            dict[i]+=1
            if dict[i]>len(nums)/2:
                return i
        return None

a = Solution()
print a.majorityElement([1,1,1,3,2,2])