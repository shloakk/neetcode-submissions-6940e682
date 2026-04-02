class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.searchMin(nums, target, 0, len(nums)-1)

    def searchMin(self, nums, target, left, right):
        if left > right:
            return -1
        
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                return self.searchMin(nums, target, left, mid - 1)
            else:
                return self.searchMin(nums, target, mid + 1, right)
        
        else:
            if nums[mid] < target <= nums[right]:
                return self.searchMin(nums, target, mid + 1, right)
            else:
                return self.searchMin(nums, target, left, mid - 1)