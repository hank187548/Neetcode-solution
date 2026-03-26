class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
    
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[right])
            res = max(res, right - l + 1 )
        return res
        