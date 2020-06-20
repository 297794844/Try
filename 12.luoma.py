class Solution1:
    def intToRoman(self, num):
        n = num
        roman = ""
        div = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = [
            "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV",
            "I"
        ]
        while n != 0:
            for i in range(len(div)):
                d = div[i]
                times = n // d
                if times != 0:
                    roman = roman + (times) * romans[i]
                    n = n - d * times
        return roman

a = Solution1()
b = 4444
print(a.intToRoman(b))
c="11   1\n"
print(c)
print(c.strip())
print('1')


