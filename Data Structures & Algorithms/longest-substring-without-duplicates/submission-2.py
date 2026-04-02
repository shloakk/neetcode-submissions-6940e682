class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        window = set()
        i = 0
        j = 0
        while i < len(s) and j < len(s):
            print(i,j, s[i:j])
            if s[j] not in window:
                window.add(s[j])
                j += 1
            else:
                window.remove(s[i])
                i += 1
            if j-i > longest:
                longest = j-i
        return longest
