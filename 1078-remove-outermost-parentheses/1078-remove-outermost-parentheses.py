class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        bal = 0
        res = []

        for char in s:
            if char == "(":
                if bal >0:
                    res.append(char)
                bal +=1
            else:
                bal -=1
                if bal >0:
                    res.append(char)

        return "".join(res)
