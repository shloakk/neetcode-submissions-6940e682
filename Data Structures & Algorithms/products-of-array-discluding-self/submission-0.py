class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [nums[0]]
        suffix_product = [1]

        for num in nums[1:]:
            prefix_product += [num * prefix_product[-1]]
        
        i = len(nums) - 1
        while i >= 1:
            suffix_product.insert(0, nums[i] * suffix_product[0])
            i -= 1
        
        output = [suffix_product[0]]
        for i in range(1, len(nums)):
            output += [(prefix_product[i-1] * suffix_product[i])]
        return output