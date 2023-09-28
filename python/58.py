class Solution(object):
    def lengthOfLastWord(self, s):
        s.strip(" ")
        su = s.split(" ")
        print(su)

        su = [x for x in su if x != '']
        if len(su) == 0:
            return 0
        else:
            return len(su[-1])


S = Solution()
print(S.lengthOfLastWord("   fly me   to   the moon  "))
