#!/usr/bin/env python
# encoding: utf-8

# The key is 3 states and 5 edges for state transition. 3 states are notHold (stock), hold (stock),
# and notHold_cooldown. The initial values of the latter two are negative infinity since they are meaningless,
# i.e. you won't hold stocks at first and there's no cooldown at first. The 5 edges:
#
# hold -----do nothing----->hold
#
# hold -----sell----->notHold_cooldown
#
# notHold -----do nothing -----> notHold
#
# notHold -----buy-----> hold
#
# notHold_cooldown -----do nothing----->notHold

# 一共有三种状态，手上有货，手上没货，手上没货但是此时处于冷却状
# 可以理解为当天开盘的时候的状态，例如当天开盘的时候状态是hold，则当天的状态可以变为notholdcooldown,(卖出了),亦可以变为hold,(没卖)
# 早上状态为nothold,则当天的状态可以变为hold(买入),notcold(不买)
# 早上状态为cooldown,则当天的状态变为nothold(冷却过去了)
# 很不错的题目
class Solution(object):
    def maxProfit(self, prices):
        notHold, notHold_cooldown, hold = 0, float('-inf'), float('-inf')
        for p in prices:
            print hold, notHold, notHold_cooldown
            hold, notHold, notHold_cooldown = max(hold, notHold - p), max(notHold, notHold_cooldown), hold + p
        return max(notHold, notHold_cooldown)

a = Solution()
prices = [1,4,2,8,5,7]
a.maxProfit(prices)