class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minimum = min([len(x) for x in strs])
        pref = ""
        for x in range(minimum):
            firsts = [s[x] for s in strs]
            if len(set(firsts)) == 1:
                pref += firsts[0]
            else:
                break
        
        return pref