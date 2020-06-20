class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shorest = min(strs, key=len)
        # 转换为枚举对象
        for i_th, letter in enumerate(shorest):
            for other in strs:
                if other[i_th] != letter:
                    return shorest[:i_th]
        return shorest

A = Solution()
B = ['flower', 'flow', 'flosda']
A.longestCommonPrefix(B)