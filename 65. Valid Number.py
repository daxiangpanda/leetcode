import re
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if 'e' in s:
            new = s.split('e')
            for i in new:
                if not i.strip().isdigit():
                    return False
            return True
        elif '.' in s:
            if len(s.split('.'))>2:
                return False
            elif s.strip().startswith('.'):
                return s.strip().split('.')[1].isdigit()
            elif s.strip().endswith('.'):
                return s.strip().split('.')[0].isdigit()
            else:
                for i in s.strip().split('.'):
                    if not i.strip().isdigit():
                        return False
                return True
        else:
            return s.strip().isdigit()

a = Solution()
print a.isNumber('0..')