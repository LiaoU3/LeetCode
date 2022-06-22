class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(' ')
        res = ""
        for word in s_list:
            for i in range(len(word)-1, -1, -1):
                res += word[i]
            res +=' '
        return res[:-1]