class Solution:

    def encode(self, strs: List[str]) -> str:
        # Append length(s) + "#" + s

        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res
        # 2#hi10#HelloWorld#3#Tie

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        # Once we move through the whole string, return
        while i < len(s):
            j = i   
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            res.append(s[i : i + length])
            i += length

        return res

