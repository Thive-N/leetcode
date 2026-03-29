class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return (set([s1[1],s1[3]]) == set([s2[1],s2[3]])) and (set([s1[2],s1[0]]) == set([s2[2],s2[0]]))

if __name__ == '__main__':
    s = Solution()
    a = s.canBeEqual('abcd','cdab')
    print(a)