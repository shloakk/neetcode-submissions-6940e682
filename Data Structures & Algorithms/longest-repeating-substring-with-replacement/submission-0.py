class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        count = {}

        left = 0
        maxFreqChar = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxFreqChar = max(maxFreqChar, count[s[right]])

            while (right - left + 1) - maxFreqChar > k:
                count[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)

        return longest