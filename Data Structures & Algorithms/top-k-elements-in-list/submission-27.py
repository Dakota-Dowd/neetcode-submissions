class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # input = array of integers ex. nums = [1,2,3, 3] k = 1
        # output = Array of the k most frequent elements in nums ex. [3]

        # Test Cases
        # nums = [1] k = 1
        # nums = [-1000, -1000, 1000, 5, 5] k = 2
        # nums = [1,2,3,4,5] k = 5

        if len(nums) == k:
            return nums
        if len(nums) == 1:
            return nums
        
        # Create a dictionary
        # Loop through nums
        # if nums[i] isn't in dictionary, add to dictionary and set initial value to 1
        # Else, increase dicationary value by 1
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] = count[num] + 1
        
        # Create output list
        # Loop through the dictionary k times
        # Append key of max value to output list
        # Remove that item from the dictionary
        # return Output

        output = []
        for i in range(k):
            max_item = list(count.keys())[0]
            for item in count:
                if count[item] > count[max_item]:
                    max_item = item
            del count[max_item]
            output.append(max_item)

        return output
