class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = {}
        for x in range(len(nums)):
            if nums[x] not in freq:
                freq[nums[x]] = 1
            else:
                freq[nums[x]] +=1
        freqList = list(freq.values())
        for x in range(len(freqList)):
            if freqList[x]%2!=0:
                return False
        return True
        
        