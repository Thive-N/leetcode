class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        f = False
        e = False

        for x in s:
            if x == "1":
                if e:
                    return False
                elif f:
                    continue
                else:
                    f = True
            else:
                if f:
                    e = True
        return True
