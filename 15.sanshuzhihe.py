class Solution():
    def sanshuzhihe9(self, str):
        c = []
        for i in range(0, len(str)):
            m = i+1
            for j in range(m, len(str)):
                n = j+1
                for k in range(n, len(str)):
                    if str[i] + str[j] + str[k] == 0:
                        first = [str[i], str[j], str[k]]
                        c.append(sorted(first))

        d = [c[i] for i in range(len(c)) if c[i] not in c[:i]]
        return d
A = Solution()
B = [-1, 0, 1, 2, -1, -4]
print(A.sanshuzhihe9(B))



