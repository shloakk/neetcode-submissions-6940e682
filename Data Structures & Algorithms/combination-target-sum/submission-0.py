class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        results = []
        def findSums(curr_sum, curr_nums, i):
            if curr_sum == target:
                results.append(curr_nums.copy())
                return
            
            if i >= len(nums) or curr_sum > target:
                return
            
            curr_nums.append(nums[i])
            findSums(curr_sum + nums[i], curr_nums, i)
            curr_nums.pop()
            findSums(curr_sum, curr_nums, i + 1)
    
        findSums(0, [], 0)
        return results