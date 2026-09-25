class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Input: array of strings ex. ["cat", "tac"]
        # Output: array of sublists ex. [["cat", "tac"], ["toe"]]
        # Test Case: ["cat", "cat"]
        # Test Case: []
        # Test Case: ["toe"]

        results = defaultdict(list)
        # Count the number of letters in each word
        # Compare against the other words
        # If they share the same count, group together
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord("a")] += 1
            results[tuple(count)].append(s)

        return list(results.values())