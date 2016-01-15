#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice,maxPro = float('inf'),0
        for price in prices:
            minPrice = min(minPrice,price)
            profit = price-minPrice
            maxPro = max(profit,maxPro)
        return maxPro