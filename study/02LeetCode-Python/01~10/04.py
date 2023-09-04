from typing import List

'''
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

示例1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2

示例2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

import math


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 这样写可以pass，但是没有用到list正序这个条件，导致消耗的内存较大
        num_list = nums1 + nums2
        num_len = len(num_list)
        num_list.sort()
        if len(num_list) % 2 == 0:
            mid = int(num_len / 2)
            return (num_list[mid-1] + num_list[mid]) / 2
        return num_list[num_len//2]

    def findMedianSortedArraysPro(self, nums1: List[int], nums2: List[int]) -> float:

        pass


if __name__ == '__main__':
    nums1 = [1,2]
    nums2 = [3,4]
    nums3 = [1, 3]
    nums4 = [2]
    print(Solution().findMedianSortedArrays(nums1,nums2))
    print(Solution().findMedianSortedArrays(nums3,nums4))



    '''
    思考：
    1、取余%，除法向下取整
    2、关键在于 "将重复字符串之前的字符都移除掉" ，这部分的设计使用set正好
    3、如果需要获得最长字串，字符串本身，则需要改造下，将set换成list
    '''
