class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Trsck x distance and y distance
        # input: Array of heights
        # Output: int, representing area of max water contained

        # Test Cases:
        # [3,5]
        # [0, 1000]
        # [1,2,3,4,5]
        # [5,5,5,5,5]

        # Intuition:
        # Goal is to track the best combo of x and y, y being the smallest height in the pair
        # Two pointer, we could try every combo but ineffecient
        # Dictionary containing key = i, value = height[i], sorted desc

        # Define l as 0 and r as length of list
        # Define greatest as 0
        # Move r to the right until it reaches the end, updating greatest, until it reaches the length of the lsit
        # Return greatest

        if len(heights) == 2:
            return min(heights[0], heights[1])
        if len(heights) == 2 and (heights[0] == 0 or heights[1] == 0):
            return 0


        l = 0
        r = 1
        greatest = 0

        while l < len(heights):
            while r < len(heights):
                distance = r - l
                min_height = min(heights[l], heights[r])
                if (distance * min_height) > greatest:
                    greatest = distance * min_height
                r += 1
            l += 1
            r = l + 1
        
        return greatest


