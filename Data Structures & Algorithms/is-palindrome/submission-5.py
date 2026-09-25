class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Input: string
        # Output: True/False, "is the string a palendrome?"
        # Test Case:
        # "123321", True
        # "Sad das", True
        # "wishy", False
        # "D00D", True
        # "t", true

        # Intuition: While i and j don't equal each other,
        #  move them closer and check if the same character
        # __________________

        # If length of s == 1, return true
        if len(s) == 1:
            return True

        # Initialize i as ffirst character and j as last character
        # While i and j are not the same, increase i and decrease j
        # if s[i] != s[j], return false
        # Otherwise return true
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i].isalnum() == False:
                i += 1
            elif s[j].isalnum() == False:
                j -= 1
            elif s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1

        return True
            
