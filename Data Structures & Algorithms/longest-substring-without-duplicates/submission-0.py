class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        biggest = 0
        start = 0
        for x in range(len(s)):
            print(freq)

            if s[x] in freq and freq[s[x]] >= start:
                start = freq[s[x]]+1       
            freq[s[x]] = x
            curr = x - start + 1
            biggest = max(biggest,curr)
        return(biggest)
        