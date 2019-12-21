class Solution:

    @staticmethod
    def convert2list(a):
        """
        把a转换成列表-字典来存储
        :param a:
        :return:
        """
        l_a = list()
        i = 0
        len_a = len(a)
        while True:
            a1 = a[i]
            if i < len_a - 1:
                a1_next = a[i + 1]
                if a1_next == "*":
                    l_a.append({a1: "*"})
                    i += 1
                else:
                    if l_a:
                        for k, v in l_a[-1].items():
                            if a1 == k:
                                if type(v).__name__ == "int":
                                    v += 1
                                l_a[-1] = {k: v}
                            else:
                                l_a.append({a1: 1})
                    else:
                        l_a.append({a1: 1})
            else:
                l_a.append({a1: 1})
                break
            i += 1
        return l_a

    @staticmethod
    def del_rep(a: str):
        """
        简化正则表达式，把*前面重复的字母去重
        """
        while "*" in a:
            i = a.index("*")
            pre = a[i - 1]
            i -= 2
            while i >= 0:
                cur_a = a[i]
                if cur_a == pre:
                    # 去掉*前面重复的
                    a = a[0:i] + a[i + 1:]
                    i -= 1
                else:
                    break
            a = a.replace("*", "#", 1)
        return a.replace("#", "*")

    def isMatch(self, s: str, p: str) -> bool:
        """
        p是规则
        s是原字符串
        :param s:
        :param p:
        :return:
        """
        if not s and not p:
            return True
        if not s and p or not p and s:
            return False
        # 下面就是s和p都不为空的情况
        p = Solution.del_rep(p)

        # 要求实现正则表达式的*与.  直接调库就是搞笑了
        # result = re.match(p+"$", s)
        # if result:
        #     return True
        # else:
        #     return False
