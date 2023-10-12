class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        t1 = []
        for x in s:
            if x == '#':
                if not len(s1) == 0:
                    s1.pop(-1)
                continue
            s1.append(x)
        for x in t:
            if x == '#':
                if not len(t1) == 0:
                    t1.pop(-1)
                continue
            t1.append(x)
        return s1 == t1
