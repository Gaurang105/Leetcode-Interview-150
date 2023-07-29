class Solution:
    def arraySign(self, nums: List[int]) -> int:
        N = len(nums)
        count = 0
        for i in range(N):
            if nums[i] < 0:
                count += 1
            if nums[i] == 0:
                return 0
        if count % 2 == 0:
            return 1
        if count % 2 != 0:
            return -1
        if count == 0:
            return 0