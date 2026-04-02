class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        strs = ""

        for char in lower_s:
            if char.isalnum():
                strs += "".join(char)

        for i in range(len(strs)-1):
            if strs[i] != strs[len(strs)-i-1]:
                return False

        return True

