class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        longest = 1
        current = 1
        for x in range(1,len(nums)):
            if nums[x]==nums[x-1]+1:
                current+=1
            elif nums[x]==nums[x-1]:
                continue
            else:
                current=1
            longest=max(longest,current)
        return longest
            
        