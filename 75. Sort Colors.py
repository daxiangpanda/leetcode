#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def swap(self,nums,a,b):
        tmp=nums[a]
        nums[a]=nums[b]
        nums[b]=tmp
        return nums

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length == 0:
            return
        low,mid,high = 0,0,length-1
        while mid <= high:
            if nums[mid] == 0:
                self.swap(nums,low,mid)
                low+=1
                mid+=1
            elif nums[mid] == 1:
                mid+=1
            else:
                self.swap(nums,mid,high)
                high-=1
    def sortColors1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length == 0:
            return
        low,high = 0,length-1
        for i in range(length):
            print nums[i]
            if nums[i] == 0:
                self.swap(nums,low,i)
                # print nums
                low+=1
            elif nums[i] == 1:
                # print nums
                continue
            elif nums[i] == 2:
                self.swap(nums,high,i)
                # print nums
                high-=1


a = Solution()
nums1 = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
nums2 = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
print a.sortColors(nums1)
print nums1
print a.sortColors1(nums2)
print nums2