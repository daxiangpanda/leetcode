#!/usr/bin/env python
# encoding: utf-8


def productExceptSelf(nums):
    size = len(nums)
    output = [1] * size
    # print nums
    # print output
    left = 1
    for x in range(size - 1):
        left *= nums[x]
        # print left
        output[x + 1] *= left
    # print output
    right = 1
    for x in range(size - 1, 0, -1):
        right *= nums[x]
        # print right
        output[x - 1] *= right
    # print output
    return output

nums = [1,2,3,4]
productExceptSelf(nums)