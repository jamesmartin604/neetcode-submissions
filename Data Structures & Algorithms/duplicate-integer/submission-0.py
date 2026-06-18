class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for x in range(len(nums)):
            if nums[x] not in freq:
                freq[nums[x]] = 1
            else:
                return True
        return False
        