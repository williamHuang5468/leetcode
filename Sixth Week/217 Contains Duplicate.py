class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        nums = sorted(nums)
        temp = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == temp:
                return True
            temp = nums[i]
        return False