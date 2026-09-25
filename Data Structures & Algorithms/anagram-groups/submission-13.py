class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Input = array of strings ex. ["act", "pots", "tops"]
        # Output = array of sublists consisting of anagrams grouped together
        #     ex. [["act"], ["pots", "tops"]]
        
        # Test Cases:
        # [""]
        # ["x"]
        # ["pots", "tops", "cat"]

        # Create a copy list
        # Create dictionary
        # loop through each item in strs
        # Create a variable that is the sorted version of the item
        # If sorted not in dictionary, add as sorted as key
        # Append strs[i] to that dictionary

        copy_list = []
        dict = {}
        for i in range(len(strs)):
            string = strs[i]
            sorted_string = sorted(string)
            key_string = "".join(sorted_string)
            if key_string not in dict:
                dict[key_string] = []
            dict[key_string].append(string)
                
        output = []
        for i in dict:
            output.append(dict[i])

        return output

