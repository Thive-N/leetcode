class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1   


def main():
    solution = Solution()
    assert solution.getCommon([1,2,3], [2,4]) == 2
    assert solution.getCommon([1,2,3], [4,5]) == -1
    assert solution.getCommon([1,2,3], [1,3]) == 1