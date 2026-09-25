class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Input: Array of nums
        # Output: true if the array contains duplicate values, else false
        # Test Case: [1,2,3,4]
        # Test Case: [1,1,1,1]
        # Test Case: [1,2,3,1]

        records = {}
        for i in nums:
            if i in records:
                return True
            else:
                records[i] = 1;
        return False
        
