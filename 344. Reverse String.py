import time

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return s
        s = list(s)
        i = 0
        j = len(s)-1
        while i<j:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1


        return ''.join(s)

a = Solution()
time.clock()
with open('345test','r') as f:
    s = f.read()
print a.reverseString(s)
print time.clock()
