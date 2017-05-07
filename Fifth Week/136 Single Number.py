'''
兩倍總和減掉 nums 總和，會得到剩下一個的數字。
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(list(set(nums)))*2 - sum(nums)

s = Solution()

assert s.singleNumber([1,2,3,1,2]) == 3
