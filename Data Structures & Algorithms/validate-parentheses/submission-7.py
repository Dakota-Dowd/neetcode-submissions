class Solution:
    def isValid(self, s: str) -> bool:
        # Input: s = string of brackets
        # output: T/F, "Are the brackets closed properly?"
        # Test Cases:
        # "["
        # "[{}]"
        # {[()}
        # {{()}}}
        # )(

        # Intuition: Add items to a stack, and pop them off if they have a matching item

        # Initialize stack = [] and dictionary of opening/closing brackets
        # Loop through s
        # if the item is an opening bracket, append it to the stack.
        # Otherwise, check if it matches the most recent item in the stack based on its dictionary value
        # if so, pop
        # Otherwise return false

        stack = []
        bracketMatches = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for c in s:
            if c in bracketMatches:
                if stack and stack[-1] == bracketMatches[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False


