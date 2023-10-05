class Solution:
    def countPoints(self, rings: str) -> int:
        m = {str(x): set() for x in range(10)}
        c = [rings[i:i+2] for i in range(0, len(rings), 2)]
        co = 0
        for col, num in c:
            m[num].add(col)

        for key in m.keys():
            if len(m[key]) == 3:
                co += 1

        return co
