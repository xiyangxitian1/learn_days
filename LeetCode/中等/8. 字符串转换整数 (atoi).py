import re


class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall(r'^[+-]?\d+', s.lstrip())), 2**31 - 1), -2**31)

    # def myAtoi(self, str: str) -> int:
    #     nums = re.match(r"\s*(([+-][0-9]+)|([0-9]*))", str)
    #     result = nums.group()
    #     result = result.strip().lstrip("0")
    #     if not result:
    #         return 0
    #     result = int(result)
    #     min_value = -2 ** 31
    #     max_value = -min_value - 1
    #     if result < min_value:
    #         return min_value
    #     if result > max_value:
    #         return max_value
    #     return result


if __name__ == '__main__':
    x = "  0000000000012345678"
    x = "words and 987"
    x = "    0000000000000   "
    x = "-000000000000001"
    x = "+"
    x = "010"
    y = Solution().myAtoi(x)
    print(y)
