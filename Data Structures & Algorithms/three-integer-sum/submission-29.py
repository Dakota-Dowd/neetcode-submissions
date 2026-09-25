from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        a = 0
        l = 1
        r = len(nums) - 1
        output = []
        
        while a < len(nums) - 2:
            # Safety Check: If pointers have crossed or met, trigger the 'a' reset immediately
            # BEFORE trying to calculate a sum that might be out of bounds!
            if l >= r:
                a += 1
                
                # Safe Duplicate Skip: Slide 'a' past identical values
                while a < len(nums) - 2 and nums[a] == nums[a - 1]:
                    a += 1
                
                # Boundary Guard: Stop if 'a' has walked too far
                if a >= len(nums) - 2:
                    break
                    
                l = a + 1
                r = len(nums) - 1
                continue # Jump back to the top to calculate the fresh sum safely
            
            # Now it is 100% safe to calculate the sum
            sum = nums[a] + nums[l] + nums[r]
            
            if sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
            else: 
                output.append([nums[a], nums[l], nums[r]])
                l += 1
                r -= 1
                
                # Safe Duplicate Skip: Slide 'l' past identical values
                while l < r and nums[l] == nums[l - 1]:
                    l += 1

        return output