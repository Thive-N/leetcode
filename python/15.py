class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        length = len(nums)

        for index in range(length - 2):
            current = nums[index]

            if index > 0 and current == nums[index - 1]:
                continue

            left = index + 1
            right = length - 1

            while left < right:
                total_sum = current + nums[left] + nums[right]

                if total_sum == 0:
                    triplets.append([current, nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total_sum < 0:
                    left += 1  # Need a larger sum
                else:
                    right -= 1  # Need a smaller sum

        return triplets