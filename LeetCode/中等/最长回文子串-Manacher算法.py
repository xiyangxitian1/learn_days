class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        s = "#" + "#".join(s) + "#"
        size = len(s)
        p = [0 for _ in range(size)]
        center = max_right = 0
        for i in range(size):
            if i < max_right:
                mirror = 2 * center - i
                p[i] = min(p[mirror], max_right - i)
            left, right = i - p[i] - 1, i + p[i] + 1
            while left >= 0 and right < size and s[left] == s[right]:
                left -= 1
                right += 1
                p[i] += 1

            if i + p[i] > max_right:
                max_right = i + p[i]
                center = i
        max_len = max(p)
        index = p.index(max_len)
        return s[index - max_len:index + max_len + 1].replace("#", "")


if __name__ == '__main__':
    y = Solution().longestPalindrome("babad")
    print(y)
