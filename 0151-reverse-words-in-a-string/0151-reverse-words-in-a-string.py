class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        val = s.split()
        reversed_word = val[::-1]

        return " ".join(reversed_word) 