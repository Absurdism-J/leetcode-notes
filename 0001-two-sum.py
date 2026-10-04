# 思路：按索引顺序取数,利用for嵌套判断剩余数是否等于target减指定数,最后按顺序返回索引
# 时间复杂度：O(n^2)  空间复杂度：O(1)
# 坑：一开始无思路看题解,实现过程需注意语句缩进以及range函数

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] == target- nums[i]:
                    return [i,j]
        return []
