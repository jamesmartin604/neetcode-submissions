class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for x in range(len(strs)):
            res.append(len(strs[x]))
            res.append("#")
            res.append(strs[x])
        encodedStr = ""
        for x in res:
            encodedStr+=str(x)
        return encodedStr

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            curr = 0
            while s[i].isdigit():
                curr = curr * 10 + int(s[i])
                i+=1
            i+=1
            res.append(s[i:i+curr])
            i+=curr
        return res
