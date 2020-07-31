class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            'I': 1, 
            'V': 5,
            'X': 10, 
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        c = 0
        p = 0
        for i in range(len(s)):
            c = dict[s[i]]
            if c > p:
                total = total + c - 2 * p
            else:
                total += c
            p = c
        return total
