#!/usr/bin/env python
# encoding: utf-8
# python 的多维数组的初始化的方法是[[0 for col in range] for row in range]
# 而不是res = [[0]*(n+1)]*(m+1) 被这个肯惨了
# 主要思路：
# 从左上到右下和的最大值
# 动态规划问题
# 主要表达式为：res[i][j] = min(res[i-1][j],res[i][j-1])+grid[i][j]
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        res = [[0 for col in range(n)] for row in range(m)]
        # print res

        for i in range(m):
            for j in range(n):
                # print grid[i][j]
                # print res
                if i == 0:
                    res[i][j] = res[i][j-1]+grid[i][j]
                elif j == 0:
                    res[i][j] = res[i-1][j] + grid[i][j]
                else:
                    res[i][j] = min(res[i-1][j],res[i][j-1])+grid[i][j]
        return res[m-1][n-1]

a = Solution()
print a.minPathSum([[1,2,3],[3,2,1]])
