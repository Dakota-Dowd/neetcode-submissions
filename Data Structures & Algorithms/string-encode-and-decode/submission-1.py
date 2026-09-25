class Solution:

    def encode(self, strs: List[str]) -> str:
        # Append each item from the list to the string
        new_string = ""
        for s in strs:
            new_string += str(len(s)) + "#" + s
        
        return new_string

    def decode(self, s: str) -> List[str]:
        # loop through each character in the string
        # Use a pointer to determine char length of the int
        # set length of character to int
        # new string = chars in range of pointer to length of chars

        res = []
        i = 0

        # Loop through each char in the string
        while i < len(s):
            # Line up i and j
            j = i   
            # Move j to the right until it hits #
            while s[j] != "#":
                j += 1
            # Set the length to the distance between i and j
            length = int(s[i:j])
            # Have i pass j
            i = j + 1
            # Add the characters from i to (i + the length)
            res.append(s[i : i + length])
            # Move i to the end of the string
            i += length
        return res
        