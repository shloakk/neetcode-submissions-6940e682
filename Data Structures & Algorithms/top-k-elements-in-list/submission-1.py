class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in hm:
            freq = hm[num]
            buckets[freq].append(num)
        
        output = []
        i = len(nums)
        while len(output) < k:
            l = len(buckets)
            if l > 0:
                output += buckets[i]
            i -= 1
        
        return output