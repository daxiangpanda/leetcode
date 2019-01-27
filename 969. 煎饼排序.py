# 给定数组 A，我们可以对其进行煎饼翻转：我们选择一些正整数 k <= A.length，然后反转 A 的前 k 个元素的顺序。我们要执行零次或多次煎饼翻转（按顺序一次接一次地进行）以完成对数组 A 的排序。

# 返回能使 A 排序的煎饼翻转操作所对应的 k 值序列。任何将数组排序且翻转次数在 10 * A.length 范围内的有效答案都将被判断为正确。

# 示例 1：

# 输入：[3,2,4,1]
# 输出：[4,2,4,3]
# 解释：
# 我们执行 4 次煎饼翻转，k 值分别为 4，2，4，和 3。
# 初始状态 A = [3, 2, 4, 1]
# 第一次翻转后 (k=4): A = [1, 4, 2, 3]
# 第二次翻转后 (k=2): A = [4, 1, 2, 3]
# 第三次翻转后 (k=4): A = [3, 2, 1, 4]
# 第四次翻转后 (k=3): A = [1, 2, 3, 4]，此时已完成排序。 
# 示例 2：

# 输入：[1,2,3]
# 输出：[]
# 解释：
# 输入已经排序，因此不需要翻转任何内容。
# 请注意，其他可能的答案，如[3，3]，也将被接受。


# 思路：1 遍历 寻找最大位置 然后在最大值位置翻转，然后再将整个列表翻转
#      2 重复1 直到有序

import numpy as np
class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        def isSortedList(l):
            if(len(l) <= 1):
                return True
            for i in range(len(l) - 1):
                if(l[i] < l[i-1]):
                    continue
                else:
                    return False
            return True
        
        def findMaxIndex(l):
            return l.index(max(l))
        res = []
        lastMaxIndex = len(A) - 1
        k = len(A) - 1
        while( not isSortedList(A)):
            maxIndex = findMaxIndex(A[:lastMaxIndex])
            if(maxIndex == 0):
                res.append(maxIndex+1)
                break
            A = A[:maxIndex+1][::-1] + A[maxIndex+1:]
            res.append(maxIndex+1)
            A = A[:k+1][::-1] + A[k+1:]
            res.append(k+1)
            k-=1
            lastMaxIndex = maxIndex
        return res

A = Solution()
print(A.pancakeSort([3,2,4,1]))