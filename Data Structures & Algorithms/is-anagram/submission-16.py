class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Input: two strings s and t
        # true/false, answering "are s and t anagrams?"
        # Test Case: s = "racecar" t = "carrace" (True)
        # Test Case: s = "racecar" t = "cartrace" (False)

        if len(s) != len(t):
            return False

        dict_s = {}
        dict_t = {}

        for i in range(len(s)):
            dict_s[s[i]] = 1 + dict_s.get(s[i], 0)
            dict_t[t[i]] = 1 + dict_t.get(t[i], 0)
        return dict_s == dict_t
