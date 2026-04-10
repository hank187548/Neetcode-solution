from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        
        # if len(t) > len(s):
        #     return ""

        # min_len = float('inf')
        # min_str = ""

        # t_count = Counter(t)

        # for i in range(len(s)):
        #     for j in range(i + len(t),len(s) + 1):
        #         sub = s[i:j]

        #         sub_count = Counter(sub)

        #         is_valid = True

        #         for char, required_count in t_count.items():
        #             if sub_count[char] < required_count:
        #                 is_valid = False
        #                 break
                
        #         if is_valid:
        #             if len(sub) < min_len:
        #                 min_len = len(sub)
        #                 min_str = sub

        # return min_str

        if t == "":
            return ""
        
        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                # update result

                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]: # feat: decrement 'have' only when window char count falls below target
                    have -= 1
                l += 1
            
        resl, resr = res
        return s[resl:resr + 1]









        