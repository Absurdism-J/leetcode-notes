# 思路：哈希表记账——查 target-num 是否见过，见过即配对；没见过就把当前数入账
# 时间复杂度：O(n)  空间复杂度：O(n)  —— 空间换时间，字典 O(1) 查询是提速根源
# 坑：必须先查后存，否则 target=2*num 时会错用自己配对
from typing import List
class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for i, num in enumerate(nums):
            if target - num in hash_table:
                return [hash_table[target - num], i]  # 先存储在哈希表的数,其下标实际在列表中也靠前
            hash_table[num] = i
        return []