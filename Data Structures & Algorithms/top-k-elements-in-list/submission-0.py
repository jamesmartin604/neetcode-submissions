class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashDict = {}
        for x in nums:
            if x not in hashDict:
                hashDict[x] = 1
            else:
                hashDict[x] += 1
        sortedDict = dict(sorted(hashDict.items(),key=lambda item:item[1],reverse=True))
        newList = list(sortedDict.keys())
        res = []
        for x in range(k):
            res.append(newList[x])
        return res

        