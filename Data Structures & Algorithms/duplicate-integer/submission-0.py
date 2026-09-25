class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}

        for i in range(len(nums)):
            if nums[i] in dict:
                return True
            else:
                dict[nums[i]] = nums[i]
        return False