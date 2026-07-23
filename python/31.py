import itertools
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        next_perm = sorted(list(itertools.permutations(nums)))
        for i in range(len(next_perm)):
            if next_perm[i] == tuple(nums):
                nums[:] = next_perm[(i + 1) % len(next_perm)]
                break
        
        
def main():
    sol = Solution()
    nums = [1, 1,5]
    sol.nextPermutation(nums)
    print(nums)
 
if __name__ == "__main__":
    main()