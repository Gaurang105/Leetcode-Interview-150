class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_num_str = ''
        for c in s:
            if c.isalnum():
                alpha_num_str += c.lower()
        if alpha_num_str == alpha_num_str[::-1]:
            return True
        else:
            return False