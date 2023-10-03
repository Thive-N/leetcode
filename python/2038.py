class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        ca = 0
        cv = 0

        for a, b, c in zip(colors, colors[1:], colors[2:]):
            if 'A' == a == b == c:
                ca += 1
            elif 'B' == a == b == c:
                cv += 1

        return ca > cv
