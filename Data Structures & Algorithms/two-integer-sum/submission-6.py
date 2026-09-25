class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dict:
                return [min([i, nums.index(diff)]), max([i, nums.index(diff)]) ]
            dict[nums[i]] = i