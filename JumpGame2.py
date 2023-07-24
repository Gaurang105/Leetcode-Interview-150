class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        l = r = 0  # this will tell what portion to we are applying BFS

        while r < n - 1:
            farthest = 0
            for i in range(l, r+1): # r+1 for inclusion
                farthest = max(farthest, i+nums[i])
            l = r+1
            r = farthest
            res += 1
        return res
