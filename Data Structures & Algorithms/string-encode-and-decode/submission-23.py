class Solution:
    # Test Cases: 
    # []
    # ["%4join", "apple", "pear"]
    # ["Hello", "World"]


    # Input: List of strings ["Hello", "World"]
    # Output: Encoded String
    def encode(self, strs: List[str]) -> str:
        # Define a divider
        # Define a blank string
        # For each item in the list, count the number of characters
        # Append divider and int  and divider to string, append  item to string
        # Return string
        divider = "%"
        output = ""
        for i in strs:
            count = 0
            for char in i:
                count += 1
            count = str(count)
            output += count
            output += divider
            output += i
        return output

    # input: Encoded Strings
    # output: original list of strings
    def decode(self, s: str) -> List[str]:
        # Define i = 0 and j = 0
        # jump = "", new_string = "", output = []
        # Loop j through each char in string
        # If string i is %, move j until j=%, appending the numbers to the jump string
        # Move j jump number of times, appending each char j is on tp new_string
        # Append string to output
        # Jump i to j + 1
        # Repeat until j + 1 > length of string
        # Return output

        i = 0
        j = 0
        jump = ""
        new_string = ""
        output = []
        while j + 1 < len(s):
            while s[j] != "%":
                j += 1
            jump = int(s[i:j])
            new_string = s[j + 1:j + 1 + jump]
            output.append(new_string)
            i = j + 1 + jump
            j = i

        return output