import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        len1 = len(s)
        a, b = 0, len1 - 1
        while a < b:
            a_ord = ord(s[a])
            if not (48 <= a_ord <= 57 or 97 <= a_ord <= 122 or 65 <= a_ord <= 90):
                a += 1
                continue
            b_ord = ord(s[b])
            if not (48 <= b_ord <= 57 or 97 <= b_ord <= 122 or 65 <= b_ord <= 90):
                b -= 1
                continue
            if s[a] != s[b]:
                return False
            a += 1
            b -= 1

        return True


def isPalindrome1(self, s: str) -> bool:
    if not s:
        return True
    s = re.sub("[^a-zA-Z0-9]", "", s)
    print(s)
    if not s:
        return True
    s = s.lower()
    len1 = len(s)
    a, b = 0, len1 - 1
    while a < b:
        if s[a] != s[b]:
            return False
        a += 1
        b -= 1

    return True


if __name__ == '__main__':
    x = "A man, a plan, a canal: Panama"
    # x = "a."
    y = Solution().isPalindrome(x)
    print(y)
