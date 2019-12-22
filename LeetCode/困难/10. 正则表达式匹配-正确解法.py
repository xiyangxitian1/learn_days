class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        p是规则
        s是原字符串
        # 方法一 回溯法  需要的时间与空间高，但是能用这外方法解出来也说明有思路
        :param s:
        :param p:
        :return:
        """
        # 如果不包含*
        # if "*" not in s:
        #     if not p: return not s
        #     part0 = bool(s) and p[0] in {s[0], "."}
        #     return part0 and self.isMatch(s[1:], p[1:])

        if not p:
            return not s
        part0 = bool(s) and p[0] in {s[0], "."}
        if len(p) >= 2 and p[1] == "*":
            return self.isMatch(s, p[2:]) or part0 and self.isMatch(s[1:], p)
        else:
            return part0 and self.isMatch(s[1:], p[1:])
