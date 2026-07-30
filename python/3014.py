class Solution:
    def minimumPushes(self, w):
        i = len(w)
        x = (i//8)
        return (x*(x+1)*4)+((i%8)*(x+1))