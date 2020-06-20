class Solution:
    def gethuiwenzichuan(self, s):
        len_whole = len(s)
        i = len_whole-1
        j = 0
        while j+i<=len_whole-1:
            j = 0
            while i and j+i <= len_whole-1:
                sub_str = s[j:j+i+1]
                sub_str_rever = list(reversed(sub_str))
                if sub_str == sub_str_rever:
                    print(sub_str)
                    return(list(sub_str))
                j += 1
            i =i-1
a = Solution()
B = ['d', 'a', 'b', 'a', 's']
a.gethuiwenzichuan(B)
