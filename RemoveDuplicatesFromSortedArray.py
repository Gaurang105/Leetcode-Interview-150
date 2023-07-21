class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # N = len(nums)
        # if N==0:
        #     return 0
        # count = 1
        # for i in range(1,N):
        #     if nums[i] != nums[i-1]:
        #         nums[count] = nums[i]
        #         count += 1
        # return count

        if len(nums) == 0:
            return 0

        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l

