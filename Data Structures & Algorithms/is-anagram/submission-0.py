class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        sArr = []
        for x in range(len(s)):
            sArr.append(s[x])
        tArr = []
        for x in range(len(t)):
            tArr.append(t[x])
        return sorted(tArr) == sorted(sArr)

        
        
        