class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        N = len(needle)
        H = len(haystack)

        for i in range(H-N+1):
            if haystack[i: i+N] == needle:
                return i
        return -1