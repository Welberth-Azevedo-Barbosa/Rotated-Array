class Solution:
    def findMin(self, nums: List[int]) -> int:

        low, high = 0, len(nums) - 1

        while low <= high:

            if nums[low] <= nums[high]:
                return nums[low]

            mid = (low + high)//2

            if nums[low] > nums[mid]:
                high = mid
            else:
                low = mid + 1
