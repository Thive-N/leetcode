class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1_000_000_007

        value_count = r - l + 1
        state_count = 2 * value_count

        def matrix_multiply(A, B):
            result = [[0] * state_count for _ in range(state_count)]

            for row in range(state_count):
                for mid in range(state_count):
                    if A[row][mid] == 0:
                        continue

                    a_val = A[row][mid]

                    for col in range(state_count):
                        if B[mid][col] == 0:
                            continue

                        result[row][col] = (
                            result[row][col] + a_val * B[mid][col]
                        ) % MOD

            return result

        transition = [[0] * state_count for _ in range(state_count)]

        for x in range(value_count):
            for y in range(x + 1, value_count):
                transition[x][value_count + y] = 1
            for y in range(x):
                transition[value_count + x][y] = 1

        power_matrix = [[0] * state_count for _ in range(state_count)]
        for i in range(state_count):
            power_matrix[i][i] = 1

        exponent = n - 1

        while exponent > 0:
            if exponent & 1:
                power_matrix = matrix_multiply(power_matrix, transition)

            transition = matrix_multiply(transition, transition)
            exponent >>= 1

        total = 0
        for row in range(state_count):
            total = (total + sum(power_matrix[row])) % MOD

        return total

  
if __name__ == "__main__":
    solution = Solution()
    n = 3
    l = 1
    r = 3
    result = solution.zigZagArrays(n, l, r)
    print(result)  # Output: 10