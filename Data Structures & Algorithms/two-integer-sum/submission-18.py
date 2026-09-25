class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Input: nums, an array of integers. target, an integer
        # Output: indices: i, j  - nums[i] + nums[j] == target and i != j
            # Return the smaller indice first

        # Test Case: target = 10 nums = [1,2,7,5,3]
            # Output: [2, 4]
        # Test Case: target = 1000, nums = [999, 10, 1]
            # Output: [0,2]

        if len(nums) == 2:
            return [0,1]

        record = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if (diff in record):
                return [min(i, record[diff]), max(i, record[diff])]
            record[nums[i]] = i

                
