#!/usr/bin/env python
# encoding: utf-8
# 这题目还是挺给力的，用动态规划的方法可以解决。
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        sum = nums[0]
        maxResult = nums[0]
        for i in range(1,len(nums)):
            # print sum
            if sum<0:
                sum = 0
            sum = max(nums[i],nums[i]+sum)
            if maxResult<sum:
                maxResult = sum

        return maxResult

a = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print a.maxSubArray(nums)