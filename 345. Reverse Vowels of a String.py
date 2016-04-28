import time

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return s
        s = list(s)
        vowels = list('aeiouAEIOU')
        i = 0
        j = len(s)-1
        while i<j:
            if s[i] in vowels and s[j] in vowels:
                s[i],s[j] = s[j],s[i]
                i+=1
                j-=1
            elif s[i] not in vowels:
                i+=1
                # continue
            elif s[j] not in vowels:
                j-=1
                # s = ??self.swap(s,i,j)
                # i+=1
                # j-=1
                # continue
        return ''.join(s)

a = Solution()
time.clock()
with open('345test','r') as f:
    s = f.read()
print a.reverseVowels(s)
print time.clock()
