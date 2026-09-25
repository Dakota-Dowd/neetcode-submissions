class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) # Creating a list of 1's the size of nums

        # First Pass, Prefix: An array of elements that are the cumulative product of all items to the left of it
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        # Second Pass: Multiply each prefix by the postfix, (the product of all items to the right of it)
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res