#!/usr/bin/env python
# encoding: utf-8
# my code
# import itertools
# class Solution(object):
#     def judge(self,s1,s2):
#         for i in s1:
#             if i in s2:
#                 return False
#         return True
#     def maxProduct(self, words):
#         """
#         :type words: List[str]
#         :rtype: int
#         """
#         maxlen = 0
#         new = itertools.combinations(words,2)
#         for i in new:
#             if self.judge(i[0],i[1]):
#                 len1 = len(i[0])*len(i[1])
#                 if maxlen<len1:
#                     maxlen = len1
#         return maxlen

# other code
# 改进的思想：原来算法里面判断单词之间是否存在相同字母的复杂度太高
# 注意到题目中说明的单词中只存在小写字母，
# 可以对这一点进行优化
# 用位运算的方法
# 进行预处理

# 改进之后的算法：
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # maps用来记录words中各个单词中字母的各个是否出项
        words = sorted(words,key = lambda i:len(i))
        # print words
        maps = [0]*len(words)
        for i in range(len(words)):
            bits = 0
            for j in range(len(words[i])):
                c = words[i][j]
                bits = bits|(1<<(ord(c)-ord('a')))
            maps[i] = bits
        # print maps
        maxlen = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if maps[i]&maps[j] == 0:#判断是否存在相同的字母
                    # print maxlen
                    # print words[i],words[j]
                    maxlen = max(maxlen,len(words[i])*len(words[j]))
                    # break # 后面的不需要判断
        return maxlen

a = Solution()
words = ["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"]
print a.maxProduct(words)

