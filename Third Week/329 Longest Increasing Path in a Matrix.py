class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        for i in matrix:
            for j in i:
                print(j, i)
        

s = Solution()

nums = [
  [8,4]
]

assert s.longestIncreasingPath(nums) == [8, 4]

# Basic

nums = [
  [8,4],
  [9,0]
]

assert s.longestIncreasingPath(nums) == [8, 4, 0]

# Example
nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]

assert s.longestIncreasingPath(nums) == [1, 2, 6, 9]

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
assert s.longestIncreasingPath(nums) == [3, 4, 5, 6]


