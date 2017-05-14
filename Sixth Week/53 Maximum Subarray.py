class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        initValue = nums[0]
        dp = []
        dp.append(initValue)
        m = initValue
        for i in range(1, size):
            consequenceValue = dp[i-1]+nums[i]
            dp.append(max(consequenceValue, nums[i]))
            m = max(m, dp[i])
        return m

s = Solution()
assert s.maxSubArray([1,2,3,4,5]) == 15
assert s.maxSubArray([1,2,-1,3,-4,5]) == 6