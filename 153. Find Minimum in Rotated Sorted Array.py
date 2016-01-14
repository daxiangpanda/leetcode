#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min=0
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]:
                continue
            min = i+1
            break
        return nums[min]