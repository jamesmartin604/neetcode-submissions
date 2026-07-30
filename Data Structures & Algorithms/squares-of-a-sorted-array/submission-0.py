class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = []
        for x in nums:
            squared.append(x**2)
        squared.sort()
        return squared
        