class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashDict = {}
        for x in range(len(nums)):
            difference = target - nums[x]
            if difference in hashDict:
                return [hashDict[difference], x]
            hashDict[nums[x]] = x