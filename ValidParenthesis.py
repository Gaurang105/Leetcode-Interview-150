class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapp = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in mapp:
                if stack and stack[-1] == mapp[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False