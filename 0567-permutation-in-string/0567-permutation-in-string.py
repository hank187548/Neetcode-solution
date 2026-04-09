class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        len1, len2 = len(s1), len(s2)

        if len1 > len2 :
            return False
        
        sorted_s1 = sorted(s1)

        for i in range(len2 - len1 + 1):
            sorted_str = sorted(s2[i:i + len1:])

            if sorted_s1 == sorted_str:
                return True
        
        return False