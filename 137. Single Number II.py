#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (3*sum(list(set(nums)))-sum(nums))/2