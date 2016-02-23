#!/usr/bin/env python
# encoding: utf-8
# 不太懂
class Solution(object):
    def rotate(self, matrix):
        n=len(matrix)
        for i in range(0,n):
            for j in range(i+1,n):
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp

        for i in range(0,n):
            for j in range(0,n//2):
                temp=matrix[i][j]
                matrix[i][j]=matrix[i][n-j-1]
                matrix[i][n-j-1]=temp