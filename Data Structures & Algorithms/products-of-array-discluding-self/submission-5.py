class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1]*len(nums)
        product = 1
        for i in range(len(nums)):
            for j in range(len(output)):
                if j == i:
                    continue
                else:
                    output[j] = output[j] * nums[i]
        return output