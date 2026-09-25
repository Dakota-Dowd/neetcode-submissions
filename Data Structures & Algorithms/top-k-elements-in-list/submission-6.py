class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket approach
        # Index = number of times appeared
        # value = list of numbers that appear that many times

        bucket = [[] for i in range(len(nums) + 1)]
        count = {}
        results = []
        
        # 1. Count Frequencies
        # Loop through the values of nums and add them as keys to the dictionary
        # The value of the key will be the appearance counts
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # 2. Map count (key) to bucket index
        for num, freq in count.items():
            bucket[freq].append(num)

        # 3. Collect top k by iterating backwards through bucket
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res

        

