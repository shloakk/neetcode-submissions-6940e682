class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_water = 0
        
        while i < j:
            left_height = heights[i]
            right_height = heights[j]
            
            curr_water = min(left_height, right_height) * (j - i)
            max_water = max(max_water, curr_water)
            
            if left_height < right_height:
                i += 1
            else:
                j -= 1
        
        return max_water