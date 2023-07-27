class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

### Beats 65% 
        dict_s = {}
        dict_t = {}

        for char in s:
            if char in dict_s:
                dict_s[char] += 1
            else:
                dict_s[char] = 1
        for char in t:
            if char in dict_t:
                dict_t[char] += 1
            else:
                dict_t[char] = 1
        return dict_s == dict_t

### Beats 10% - Worst Solution
        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False