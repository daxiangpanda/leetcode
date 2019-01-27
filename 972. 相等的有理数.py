# 给定两个字符串 S 和 T，每个字符串代表一个非负有理数，只有当它们表示相同的数字时才返回 true；否则，返回 false。字符串中可以使用括号来表示有理数的重复部分。

# 通常，有理数最多可以用三个部分来表示：整数部分 <IntegerPart>、小数非重复部分 <NonRepeatingPart> 和小数重复部分 <(><RepeatingPart><)>。数字可以用以下三种方法之一来表示：

# <IntegerPart>（例：0，12，123）
# <IntegerPart><.><NonRepeatingPart> （例：0.5，2.12，2.0001）
# <IntegerPart><.><NonRepeatingPart><(><RepeatingPart><)>（例：0.1(6)，0.9(9)，0.00(1212)）
# 十进制展开的重复部分通常在一对圆括号内表示。例如：

# 1 / 6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66)

# 0.1(6) 或 0.1666(6) 或 0.166(66) 都是 1 / 6 的正确表示形式。



# 做题的话 这道题暴力比常规rule更有效！太蠢了！

class Solution:
    def isRationalEqual(self, S, T):
        """
        :type S: s
        :type T: s
        :rtype: bool
        """
        return abs(self.toNum(S) - self.toNum(T)) < 1e-15
    def toNum(self,s):
        norep,rep = "",""
        n = 0
        for i in range(len(s)):
            if s[i] == '(':
                n = i
                norep = s[:i]
            elif s[i] == ')':
                rep = s[n+1:i]
            
        res = s
        if norep != '':
            res = norep
            
        if rep != '':
            res += rep*16
            
        return float(res)




S = Solution()
print(S.toNum("1.923(3)"))