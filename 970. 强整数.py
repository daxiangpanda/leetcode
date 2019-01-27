# 给定两个非负整数 x 和 y，如果某一整数等于 x^i + y^j，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个强整数。

# 返回值小于或等于 bound 的所有强整数组成的列表。

# 你可以按任何顺序返回答案。在你的回答中，每个值最多出现一次。


# 示例 1：

# 输入：x = 2, y = 3, bound = 10
# 输出：[2,3,4,5,7,9,10]
# 解释： 
# 2 = 2^0 + 3^0
# 3 = 2^1 + 3^0
# 4 = 2^0 + 3^1
# 5 = 2^1 + 3^1
# 7 = 2^2 + 3^1
# 9 = 2^3 + 3^0
# 10 = 2^0 + 3^2
# 示例 2：

# 输入：x = 3, y = 5, bound = 15
# 输出：[2,4,6,8,10,14]
 

# 提示：

# 1 <= x <= 100
# 1 <= y <= 100
# 0 <= bound <= 10^6


import math
class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        res = []
        count = 0969. 煎饼排序
        if(bound == 0):
            return []
        if(x == 1 or y == 1):
            if (x == 1 and y == 1):
                if (bound < 2):
                    return []
                else:
                    return [2]
            else:
                res.append(2)
                i = 1
                while(1 + (x * y) ** i < bound): # 写成x * y 因为可能是x = 1 或者 y = 1
                    res.append(1 + (x * y) ** i)
                    i+=1
                return res


        for i in range(int(math.log(bound) / math.log(x)) + 1):
            for j in range(int(math.log(bound) / math.log(y)) + 1):
                count += 1
                # print(i,j)
                k = x ** i + y ** j
                # print('k=',k)
                if(k<=bound):
                    res.append(k)
                else:
                    break
        # print("count:",count)
        return list(set(res))

A = Solution()
print(A.powerfulIntegers(1,2,100))