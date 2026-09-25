class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        # Iterate through set
        for num in numSet:
            # If num is the first element in a sequence, begin counting the length of the sequence
            if (num - 1) not in numSet:
                length = 1 # Reset the length of the current sequence

                # Keep adding to the length as long as we can search and find a sequential number
                while (num + length) in numSet:
                    length += 1
                
                # If the length is longer than the longest sequence, make that length the new longest
                longest = max(length, longest)
        return longest