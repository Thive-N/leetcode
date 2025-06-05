from collections import deque


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        q = deque([(0, 0)])
        seen = set()

        while q:
            i, j = q.pop()
            if (i, j) in seen:
                continue
            seen.add((i, j))
            if i >= len(s) and j >= len(p):
                return True
            elif j >= len(p):
                continue

            if j + 1 < len(p) and p[j + 1] == '*':
                q.append((i, j + 2))
                if i < len(s) and (p[j] == '.' or p[j] == s[i]):
                    q.append((i + 1, j))
            elif i < len(s) and (p[j] == '.' or p[j] == s[i]):
                q.append((i + 1, j + 1))

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isMatch("aa", "a"))  # False
    print(s.isMatch("aa", "a*"))  # True
    print(s.isMatch("ab", ".*"))  # True
    print(s.isMatch("aab", "c*a*b"))  # True
    print(s.isMatch("mississippi", "mis*is*p*."))  # False
    print(s.isMatch("ab", ".*c"))  # False
    print(s.isMatch("aaa", "a*a"))  # True
    print(s.isMatch("a", "ab*"))  # True
    print(s.isMatch("aaaaaaaaaa", "a*a*a*a*a*a*a*a*a*b"))  # False
