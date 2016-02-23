#!/usr/bin/env python
# encoding: utf-8

import itertools
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        list = itertools.combinations(range(1,10),k)
        for i in list:
            if sum(i) == n:
                res.append(i)
        return res