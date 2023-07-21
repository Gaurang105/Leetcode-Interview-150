class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # set_nums = set(nums)
        # if len(nums) != len(set_nums):
        #     return True
        # else:
        #     return False

        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

