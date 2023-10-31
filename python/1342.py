class Solution:
    def numberOfSteps(self, num: int) -> int:
        return 0 if num == 0 else num.bit_count() + (num.bit_length() - 1)
