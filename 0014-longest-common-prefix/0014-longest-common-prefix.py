class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        n = len(strs)

        for i in range(len(strs[0])):
            curr = strs[0][i]
            for st in strs[1:]:
                if i >= len(st) or st[i] != curr:
                    return strs[0][:i]
        return strs[0]