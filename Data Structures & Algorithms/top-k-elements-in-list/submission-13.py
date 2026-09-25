class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        counter = {}
        res = []

        # 1. Count frequencies
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)

        # 2. Map to bucket
        for value, freq in counter.items():
            bucket[freq].append(value)

        # 3. Grab top k
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res


        

