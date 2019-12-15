from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        nums.sort()
        for n in nums:
            a ^= n
        return a

        # 方法二 ，虽然通过了但是用了空间太多
        # if not nums:
        #     return
        # nums.sort()
        # len1 = len(nums)
        # i = 0
        # while i < len1 - 1:
        #     if nums[i] != nums[i + 1]:
        #         return nums[i]
        #     i += 2
        # return nums[-1]

        """方法一 超出时间限制"""
        # for n in nums:
        #     if nums.count(n) == 1:
        #         return n
