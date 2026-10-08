import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = list(stones)
        heapq.heapify_max(max_heap)

        while len(max_heap) > 1:
            s1 = heapq.heappop_max(max_heap)
            s2 = heapq.heappop_max(max_heap)

            if s1 != s2:
                heapq.heappush_max(max_heap, abs(s1 - s2))

        if not max_heap:
            return 0

        return heapq.heappop_max(max_heap)