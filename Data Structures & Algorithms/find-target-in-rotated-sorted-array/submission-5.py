class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Input: nums (array), target (iinteger)
        # Output: index of target 

        # Examples: T = M
        # T = L, T = R

        l = 0
        r = len(nums) - 1

        while r >= l:
            m = r + 1 // 2
            if target == nums[m]:
                return m
            # If in left side 
            if nums[l] <= nums[m]:
                if target >= nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            # If in right side
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1

                
