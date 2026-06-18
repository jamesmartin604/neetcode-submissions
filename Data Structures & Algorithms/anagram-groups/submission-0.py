class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashDict = {}
        for x in range(len(strs)):
            if(''.join(sorted(strs[x])) not in hashDict):
                hashDict[''.join(sorted(strs[x]))] = []
        for x in range(len(strs)):
            currStr = ''.join(sorted(strs[x]))
            if currStr in hashDict:
                joinedStr = ''.join(strs[x])
                hashDict[currStr] += [joinedStr]
        resList = list(hashDict.values())
        res = []
        for x in resList:
            res.append(x)
        return res