class Solution():
    def huiwen(self, data):
        d = str(data)
        d_hui = d[::-1]
        if(d == d_hui):
            return 'Yes'
        else:
            return 'No'
a = Solution()
b = 12321
print(a.huiwen(b))