class Solution(object):
    def isMonotonic(self, nums):
        decreasing = None
        curr = None
        for x in nums:
            if curr is None:
                curr = x

            else:
                if decreasing is None:
                    if x > curr:
                        decreasing = False
                    elif x < curr:
                        decreasing = True
                else:
                    if decreasing and x > curr:
                        return False
                    elif not decreasing and x < curr:
                        return False
                curr = x

        return True
