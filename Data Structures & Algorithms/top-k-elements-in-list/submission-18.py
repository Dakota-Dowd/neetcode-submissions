class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}
        bucket = [[] for i in range(len(nums) + 1)]
        results = []

        # Count frequency of elements in nums
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        # Sort w/ Bucket Sort
        for num, freq in counts.items():
            bucket[freq].append(num)

        # Return k number of high value elements
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                results.append(n)
                if len(results) == k:
                    return results

        
