class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        hm = {}
        longest = 0
        for num in nums:
            seq_len = 0
            if num - 1 not in nums_set:
                x = num
                while x in nums_set:
                    seq_len += 1
                    x += 1
            if seq_len > longest:
                longest = seq_len
        return longest