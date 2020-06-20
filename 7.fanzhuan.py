class Solution():
    def huanwei(self, a):
        b = str(a)
        l = len(b)
        a=0
        if(b[0] =='-'):
            a=1
            b = b[1:]
            d = '-'
        if(b[l-2] == '0'):
            b = b[0:l-2]
        last = b[::-1]
        if(a == 1):
            list= d + last
            return(list)
        else:
            return(last)


a = Solution()
b = -1242430
print(a.huanwei(b))



