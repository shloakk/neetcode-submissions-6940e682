class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.searchMin(nums, 0, len(nums))

    def searchMin(self, nums, left, right):
        minimum = nums[left]
        if nums[left] > nums[right-1]:
            mid = left + (right - left) // 2
            minimum = min(self.searchMin(nums, left, mid), self.searchMin(nums, mid, right))
        return minimum