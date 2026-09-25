from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        items_dict = {}
        output = []
        copy_dict = {}  # Fixed: Initialized as a dictionary, not a list []
        
        # 1. Map each number to its last seen index
        for i in range(len(nums)):
            items_dict[nums[i]] = i 

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    k = 0 - nums[i] - nums[j]
                    
                    # 2. Check if the complement exists in our map
                    if k in items_dict:
                        k_index = items_dict[k]
                        
                        # FIX: Ensure we aren't reusing the exact same index position
                        if k_index != i and k_index != j:
                            
                            # FIX: Create the triplet using values, not indices
                            output_item = [nums[i], nums[j], k]
                            
                            # FIX: Use sorted() + tuple() because lists cannot be dict keys
                            sorted_tuple = tuple(sorted(output_item))
                            
                            if sorted_tuple in copy_dict:
                                continue
                            else:
                                copy_dict[sorted_tuple] = 1
                                # FIX: Pass the item to append()
                                output.append(output_item)
                                
        return output