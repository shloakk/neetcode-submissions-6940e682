class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)

        unique_chars = {s[0]}
        l = 0
        r = 0
        s_len = len(s)
        max_len = 0

        while l != s_len-1 and r != s_len-1:
            r += 1
            right_c = s[r]

            if right_c in unique_chars:
                left_c = s[l]
                while right_c in unique_chars:
                    unique_chars.remove(left_c)
                    l += 1
                    left_c = s[l]
            
            unique_chars.add(right_c)
            if r - l + 1 > max_len:
                max_len = r - l + 1
        
        return max_len