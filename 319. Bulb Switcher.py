#!/usr/bin/env python
# encoding: utf-8

# 原题：
# There are n bulbs that are initially off.
# You first turn on all the bulbs.
# Then, you turn off every second bulb.
# On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on).
# For the nth round, you only toggle the last bulb.
# Find how many bulbs are on after n rounds.
#
# 分析：
# 第一轮将灯泡全部打开
# 第二轮关掉序号为偶数的灯泡
# 第i轮改变序号为i的倍数的灯泡的状态
# 第n轮关闭最后一个灯泡
#
# 得出最后结果为开方
import math
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))