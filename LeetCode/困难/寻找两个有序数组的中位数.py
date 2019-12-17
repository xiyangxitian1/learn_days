from typing import List


class Solution:
    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        """
        两个有序数组求中位数，问题一般化为，求两个有序数组的第k个数，当k = (m+n)/2时为原问题的解。
        怎么求第k个数？分别求出第一个和第二个数组的第 k / 2个数 a 和 b，然后比较 a 和 b，当a < b ，
        说明第 k 个数位于 a数组的第 k / 2个数后半段，或者b数组的 第 k / 2 个数前半段，问题规模缩小了一半，
        然后递归处理就行。

        时间复杂度是 O(log(m+n))
        :param nums1:
        :param nums2:
        :return:
        """
        pass


    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        """
         中位数是左右两个的数的个数相等，如果是偶数个就取中间两个数的和除以2
         这个时间复杂度不满足O(long(m+n))  m,n为两个数组的长度
        :param nums1:
        :param nums2:
        :return:
        """
        new_list = list()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                new_list.append(nums1[i])
                i += 1
            else:
                new_list.append(nums2[j])
                j += 1
        while i < len(nums1):
            new_list.append(nums1[i])
            i += 1
        while j < len(nums2):
            new_list.append(nums2[j])
            j += 1
        if len(new_list) % 2 == 0:
            middle = len(new_list) // 2
            return (new_list[middle - 1] + new_list[middle]) / 2
        else:
            return new_list[len(new_list) // 2]


if __name__ == '__main__':
    x = [1, 3]
    y = [2]
    Solution().findMedianSortedArrays(x, y)
