class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Input: nums = [int]
        # Output: number of potential consecutive ints in nums

        # Test Cases:
        # []
        # [-1,0,1]
        # [5, 3, 4, 2, 1, 9]

        # If length of nums == 0, return 0

        # Intuition: Create a dictionary of the nums, and loop through checking if item + 1 is in dict
        
        # Sort nums
        # Initialize output as 0
        # Initialize max output
        # Add items to dictionary
        # Loop through dictionary, checking if item + 1 is in dict
        # if so, increase output count by one
        # else, if output > max output set max output to output
        # Reset output to 0
        # Return max output

        if nums == []:
            return 0

        nums.sort()
        count = 1
        max_count = 1
        item_dict = {}
        for item in nums:
            if item in item_dict:
                item_dict[item] = item_dict[item] + 1
            else:
                item_dict[item] = 0

        for item in item_dict:
            if item + 1 in item_dict.keys():
                count += 1
            else:
                if count > max_count:
                    max_count = count
                count = 1
        
        return max_count

