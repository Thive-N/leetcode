class Solution:
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + (nums[i] == target)

        ans = 0
        for i in range(n):
            for j in range(i, n):
                count = pref[j + 1] - pref[i]
                if count > (j - i + 1) // 2:
                    ans += 1

        return ans