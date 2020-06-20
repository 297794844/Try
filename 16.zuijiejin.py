class Solution():
    def sanshuzhihe9(self, str, target):
        c = []
        for i in range(0, len(str)):
            m = i+1
            for j in range(m, len(str)):
                n = j+1
                for k in range(n, len(str)):
                    o = str[i] + str[j]+ str[k]
                    c.append(o)
        d = [abs(i-target) for i in c]
        k = min(d)
        return c[d.index(k)]
A = Solution()
B = [-1, 2, 1, -4]
C = 1
print(A.sanshuzhihe9(B, C))