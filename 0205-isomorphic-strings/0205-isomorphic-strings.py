class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        map_s = {}
        map_t = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            if char_s in map_s:
                if map_s[char_s] != char_t:
                    return False

            if char_t in map_t:
                if map_t[char_t] != char_s:
                    return False
            map_s[char_s] = char_t
            map_t[char_t] = char_s
        return True
        