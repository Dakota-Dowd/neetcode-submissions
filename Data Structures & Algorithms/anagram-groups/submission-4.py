class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Input: Array of strings
        # Output: array of sublists, grouped by anagram families
        # Test Case: ["may", "yam", "", "x", "x"]
        # Test Case: ["x", "x"]
        # Test Case: []
        # Test Case: ["s"]

        results = defaultdict(list)
       
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            results[tuple(count)].append(s) # [0,1,0] : ["s", "s2"]
        
        return list(results.values())