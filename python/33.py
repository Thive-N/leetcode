class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        rotation_index = left

        # normal binary search
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2

            # map mid into rotated array
            real_mid = (mid + rotation_index) % n

            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1