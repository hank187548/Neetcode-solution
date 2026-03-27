from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        d = defaultdict(int)
        res = 0

        for r in range(len(s)):
            d[s[r]] += 1
            windows_legth = r - l + 1
            max_freq = max(d.values())

            if windows_legth - max_freq > k:
                d[s[l]] -= 1

                l += 1
            res = max(res, r - l + 1)

        return res


        
        