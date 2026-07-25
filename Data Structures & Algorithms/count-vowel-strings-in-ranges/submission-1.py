class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def starsEndVowel(str) -> bool:
            first = str[0]
            last = str[len(str)-1]
            if (first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u') and (last == 'a' or last == 'e' or last == 'i' or last == 'o' or last == 'u'):
                return True
            return False
        
        res = []
        for x in range(len(queries)):
            count = 0
            for y in range(queries[x][0], queries[x][1]+1):
                if starsEndVowel(words[y]):
                    count+=1
            res.append(count)
        return res
        