class Solution():
    def zuhe(self, digit):
        cosdic = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pars",
            "8":"tuv",
            "9":"wxyz"
        }
        list = []
        strdigit = str(digit)
        for i in range(len(strdigit)):
            k = i + 1
            if(i == len(strdigit)-1):
                l = sorted(list)
                d = [l[i] for i in range(len(l)) if l[i] not in l[:i]]
                return d
            for j in cosdic[strdigit[i]]:
                for m in range(k, len(strdigit)):
                    for n in cosdic[strdigit[m]]:
                        list.append(j+n)

A = Solution()
B = 22
print(A.zuhe(B))



