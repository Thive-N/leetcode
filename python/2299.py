class Solution:
    def strongPasswordCheckerII(self, p: str) -> bool:
        if len(p) < 8:
            return False
        if not any(c.islower() for c in p):
            return False
        if not any(c.isupper() for c in p):
            return False
        if not any(c.isdigit() for c in p):
            return False
        if not any("!@#$%^&*()-+".find(c) != -1 for c in p):
            return False
        return all(a != b for a, b in zip(p, p[1:]))
