class Solution:
    def longestPalindrome(self, s: str) -> str:
        """自己写出Manacher 马拉车算法"""
        if len(s) < 2:
            return s
        # 得到预处理字符
        s0 = s
        s = "#" + "#".join(s) + "#"
        size = len(s)
        # 数组p记录了扫描过的回文子串的信息
        p = [0 for _ in range(size)]
        # 双指针，它们是一一对应的，必须同时更新
        center = max_right = 0
        # 当前遍历的中心最大扩散步数，其值等于原始字符串的最长回文子串的长度
        max_len = 1
        # 原始字符串的最长回文子串的起始位置，与 max_len 必须同时更新
        start = 1
        flag = False  # 是否需要扩散，加了并且没有提升效率，哎 , 可以不加了
        for i in range(size):
            if i < max_right:
                mirror = 2 * center - i
                # 这一行代码是Manacher算法的关键所在，结合图形来理解
                # 只有 p[mirror] = max_right-i时  才会继续扩散
                if p[mirror] == max_right - i:
                    flag = True
                    p[i] = p[mirror]
                else:
                    p[i] = min(max_right - i, p[mirror])
                    flag = False
            else:
                flag = True
            # 下一次尝试扩散的左右起点，能扩散的步数直接添加到p[i]中
            if flag:
                left, right = i - (1 + p[i]), i + (1 + p[i])
                while left >= 0 and right <= size - 1 and s[left] == s[right]:
                    left -= 1
                    right += 1
                    p[i] += 1
            # 根据 max_right 的定义，它是遍历过的 i 的 i + p[i] 的最大者
            # 如果 max_right 的值越大，进入上面 i < max_right 的判断的可能性就越大，这样就可以重复利用之前判断过的回文信息了
            if i + p[i] > max_right:
                max_right = i + p[i]
                center = i
            if p[i] > max_len:
                max_len = p[i]
                start = (i - max_len) // 2
        return s0[start:start + max_len]

    def longestPalindrome5(self, s: str) -> str:
        """自己写出Manacher 马拉车算法"""
        if len(s) < 2:
            return s
        # 得到预处理字符
        s0 = s
        s = "#" + "#".join(s) + "#"
        size = len(s)
        # 数组p记录了扫描过的回文子串的信息
        p = [0 for _ in range(size)]
        # 双指针，它们是一一对应的，必须同时更新
        center = max_right = 0
        # 当前遍历的中心最大扩散步数，其值等于原始字符串的最长回文子串的长度
        max_len = 1
        # 原始字符串的最长回文子串的起始位置，与 max_len 必须同时更新
        start = 1

        for i in range(size):
            if i < max_right:
                mirror = 2 * center - i
                # 这一行代码是Manacher算法的关键所在，结合图形来理解
                p[i] = min(max_right - i, p[mirror])
            # 下一次尝试扩散的左右起点，能扩散的步数直接添加到p[i]中
            left, right = i - (1 + p[i]), i + (1 + p[i])
            while left >= 0 and right <= size - 1 and s[left] == s[right]:
                left -= 1
                right += 1
                p[i] += 1
            # 根据 max_right 的定义，它是遍历过的 i 的 i + p[i] 的最大者
            # 如果 max_right 的值越大，进入上面 i < max_right 的判断的可能性就越大，这样就可以重复利用之前判断过的回文信息了
            if i + p[i] > max_right:
                max_right = i + p[i]
                center = i
            if p[i] > max_len:
                max_len = p[i]
                start = (i - max_len) // 2
        return s0[start:start + max_len]

    def longestPalindrome4(self, s: str) -> str:
        """自己写出Manacher 马拉车算法 (经过测试这个已经是最快的算法了。上面两个理论上会更快，但是没有得到证实。)"""
        if len(s) < 2:
            return s
        # 得到预处理字符
        s = "#" + "#".join(s) + "#"
        size = len(s)
        # 数组p记录了扫描过的回文子串的信息
        p = [0 for _ in range(size)]
        # 双指针，它们是一一对应的，必须同时更新
        center = max_right = 0
        for i in range(size):
            if i < max_right:
                mirror = 2 * center - i
                # 这一行代码是Manacher算法的关键所在，结合图形来理解
                p[i] = min(max_right - i, p[mirror])
            # 下一次尝试扩散的左右起点，能扩散的步数直接添加到p[i]中
            left, right = i - (1 + p[i]), i + (1 + p[i])
            while left >= 0 and right <= size - 1 and s[left] == s[right]:
                left -= 1
                right += 1
                p[i] += 1
            # 根据 max_right 的定义，它是遍历过的 i 的 i + p[i] 的最大者
            # 如果 max_right 的值越大，进入上面 i < max_right 的判断的可能性就越大，这样就可以重复利用之前判断过的回文信息了
            if i + p[i] > max_right:
                max_right = i + p[i]
                center = i
        max_num = max(p)
        index = p.index(max_num)
        return s[index - max_num:index + max_num + 1].replace("#", "")

    # Manacher 算法
    def longestPalindrome3(self, s: str) -> str:
        # 特判
        size = len(s)
        if size < 2:
            return s

        # 得到预处理字符串
        t = "#"
        for i in range(size):
            t += s[i]
            t += "#"
        # 新字符串的长度
        t_len = 2 * size + 1

        # 数组 p 记录了扫描过的回文子串的信息
        p = [0 for _ in range(t_len)]

        # 双指针，它们是一一对应的，须同时更新
        max_right = 0
        center = 0

        # 当前遍历的中心最大扩散步数，其值等于原始字符串的最长回文子串的长度
        max_len = 1
        # 原始字符串的最长回文子串的起始位置，与 max_len 必须同时更新
        start = 1

        for i in range(t_len):
            if i < max_right:
                mirror = 2 * center - i
                # 这一行代码是 Manacher 算法的关键所在，要结合图形来理解
                p[i] = min(max_right - i, p[mirror])

            # 下一次尝试扩散的左右起点，能扩散的步数直接加到 p[i] 中
            left = i - (1 + p[i])
            right = i + (1 + p[i])

            # left >= 0 and right < t_len 保证不越界
            # t[left] == t[right] 表示可以扩散 1 次
            while left >= 0 and right < t_len and t[left] == t[right]:
                p[i] += 1
                left -= 1
                right += 1

            # 根据 max_right 的定义，它是遍历过的 i 的 i + p[i] 的最大者
            # 如果 max_right 的值越大，进入上面 i < max_right 的判断的可能性就越大，这样就可以重复利用之前判断过的回文信息了
            if i + p[i] > max_right:
                # max_right 和 center 需要同时更新
                max_right = i + p[i]
                center = i

            if p[i] > max_len:
                # 记录最长回文子串的长度和相应它在原始字符串中的起点
                max_len = p[i]
                start = (i - max_len) // 2
        return s[start: start + max_len]

    def longestPalindrome2(self, s: str) -> str:
        """
            输入: "babad"
            输出: "bab"
            注意: "aba" 也是一个有效答案。
            解法二：Manacher 算法 (初步） 已经可以求解了，不过改进后才能达到世界顶级
        :param s:
        :return:
        """
        if not s or len(s) == 1:
            return s
        s = "#" + "#".join(s) + "#"
        # 辅助数组P计算相应位置的最长子串的长度,默认先置为0
        p = [0 for _ in range(len(s))]

        # 计算s相应位置的最长步数，也就是数组p相应位置的值
        # 因为要遍布一遍，还要求步长，所以时间复杂度为O(N**2)了。 空间复杂度为O(N)
        len1 = len(s)
        for i in range(len1):
            # 步长
            step = 0
            # 向左右扩展
            left, right = i - 1, i + 1
            while left >= 0 and right < len1:
                if s[left] != s[right]:
                    break
                step += 1
                left -= 1
                right += 1
            p[i] = step
        step = max(p)
        if step == 0:
            return s[1]
        index = p.index(step)
        # 所以是这个index 为索引扩展的是最大的,步长为step
        return s[index - step: index + step + 1].replace("#", "")

    def longestPalindrome1(self, s: str) -> str:
        """
            输入: "babad"
            输出: "bab"
            注意: "aba" 也是一个有效答案。
        :param s:
        :return:
        """
        #  解法一 中心扩展法
        # 只需要计算2n-3即可
        if not s or len(s) == 1:
            return s
        len1 = len(s)
        max_zi_s = s[0]
        for i in range(len1 - 1):
            # 算奇
            # 向两边扩展，至少是3个字符
            left, right = i - 1, i + 1
            while left >= 0 and right <= len1 - 1:
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
            max_zi_1 = s[left + 1:right]

            # 算偶
            # 向两边扩展，至少是2个字符
            left, right = i, i + 1
            while left >= 0 and right <= len1 - 1:
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
            max_zi_2 = s[left + 1:right]

            # 算出这现个中最长的
            if len(max_zi_1) < len(max_zi_2):
                max_zi_1, max_zi_2 = max_zi_2, max_zi_1
            # 和现在的最长子串进行比较
            if len(max_zi_1) > len(max_zi_s):
                max_zi_s = max_zi_1
        return max_zi_s


if __name__ == '__main__':
    y = Solution().longestPalindrome("abb")
    print(y)
