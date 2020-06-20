class Solution():
    def Maxarea(self, data):
        list = []
        for i in data:
            for j in data:
                kuan = max(set([i, j]))
                chang = abs(data.index(i) - data.index(j))
                list.append(kuan*chang)

        return max(list)
a = Solution()
b = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(a.Maxarea(b))

