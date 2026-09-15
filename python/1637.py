class Solution:
    def maxWidthOfVerticalArea(self, points):
        ans = 0

        a = [point[0] for point in points]
        a.sort()

        for i in range(1, len(points)):
            t = a[i] - a[i - 1]
            ans = max(ans, t)

        return ans