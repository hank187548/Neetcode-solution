class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = { ")":"(","}":"{","]":"["}

        for c in s:
            if c in mapping:
                if stack:
                    last_element = stack.pop()
                else:
                    return False
                if last_element != mapping[c]:
                    return False


            else:
                stack.append(c)
        return not stack

    
        