# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def get(self, index: int) -> int: pass
    def length(self) -> int: pass


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: MountainArray) -> int:
        length = mountain_arr.length()

        l, r = 1, length-2
        while l <= r:
            m = (l+r)//2
            left = mountain_arr.get(m-1)
            mid = mountain_arr.get(m)
            right = mountain_arr.get(m+1)

            if left < mid < right:
                l = m+1
            elif left > mid > right:
                r = m-1
            else:
                break

        l, r = 0, m
        while l <= r:
            m = (l+r)//2
            val = mountain_arr.get(m)
            if val < target:
                l = m + 1
            elif val > target:
                r = m-1
            else:
                return m

        l, r = m, length-1
        while l <= r:
            m = (l+r)//2
            val = mountain_arr.get(m)
            if val > target:
                l = m + 1
            elif val < target:
                r = m-1
            else:
                return m

        return -1
