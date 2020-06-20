# -*- coding: UTF-8 -*-
def isnumber( s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        for i in s:
            unicodedata.numeric(i)
        return True
    except (TypeError, ValueError):
        pass
    return False
class Solution():
    def zhuanhuan(self, data):
        s = data.lstrip()
        if(s[0] == '+' or s[0] == '-'):
            p = s[0]
            s = s[1:]
        else:
            p=''
        if(s[0].isdigit()):
            for i in s:
                if(i.isdigit()):
                    d = s[:(s.index(i)+1)]
                else:
                    break
            if(int(d) > 2**31):
                return 2**31
            else:
                c = p+d
                return c
        else:
            return 0
a = Solution()
b = ' -554413    w 55456w'
print(a.zhuanhuan(b))

