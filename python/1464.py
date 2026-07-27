class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lmax = 0
        rmax = 0

        for x in range(len(nums)):
            if nums[x] > lmax:
                rmax = lmax
                lmax = nums[x]
                continue

            if nums[x] > rmax:
                rmax = nums[x]

        print(lmax)
        print(rmax)
        return (lmax-1) * (rmax-1)