#!/usr/bin/env python
# encoding: utf-8
import itertools
class Solution(object):
    # def generateParenthesis(self, n):
    #     """
    #     :type n: int
    #     :rtype: List[str]
    #     """
    #     res = [('', 0, n)]
    #     maxn = n
    #     while maxn > 0:
    #         maxn = 0
    #         l = len(res)
    #         for i in range(l):
    #             s, b, k = res[i]
    #             if k > maxn: maxn = k
    #             if k > 0:
    #                 res[i] = (s+'(', b+1, k-1)
    #                 if b > 0:
    #                     res.append((s+')', b-1, k))
    #             elif b > 0:
    #                 res[i] = (s+')', b-1, k)
    #     return [s[0] for s in res]
    def judge(self,s):
        count = 0
        for i in s:
            if count <0:
                return False
            if i == '(':
                count+=1
            if i == ')':
                count-=1
        return True
    def generateParenthesis(self, n):
        list1 = ['(']*n+[')']*n
        result = set()
        perm = itertools.permutations(list1,2*n)
        for i in perm:
            if self.judge(''.join(i)):
                result.add(''.join(i))
        return list(result)

a = Solution()
print a.generateParenthesis(10000)