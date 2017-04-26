class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        onesList = []
        for i in nums:
            if i == 1:
                count += 1
            else:
                onesList.append(count)
                count = 0
        onesList.append(count)
        return max(onesList)
            

s = Solution()
assert s.findMaxConsecutiveOnes([1,1]) == 2
assert s.findMaxConsecutiveOnes([0,1]) == 1
assert s.findMaxConsecutiveOnes([1,0,1]) == 1
assert s.findMaxConsecutiveOnes([1,0,1,1]) == 2
assert s.findMaxConsecutiveOnes([1,0,0,1]) == 1
assert s.findMaxConsecutiveOnes([1,0,0,0,1,1,1]) == 3
