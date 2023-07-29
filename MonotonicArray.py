class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        return all(nums[i] <= nums[i+1] for i in range(n-1)) or all(nums[i] >= nums[i+1] for i in range(n-1))