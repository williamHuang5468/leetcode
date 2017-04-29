class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

'''
Input : word1, word2 (both str)
Output: int of step

# find minimum number of steps
# convert word1 to word2 , word1 -> word2
# each operation is counted as 1 step.

operations list:

1.  Insert a character
1.  Delete a character
1.  Replace a character
'''
s = Solution()

# simple example for replace, word2 of len will equal word1
firstWord = "a"
secondWord = "b"
assert s.minDistance(firstWord, secondWord) == 1

# simple example for insert, word2 of len will bigger word1
firstWord = "b"
secondWord = "ab"
assert s.minDistance(firstWord, secondWord) == 1

# simple example for delete, word1 of len will bigger word2
firstWord = "ab"
secondWord = "b"
assert s.minDistance(firstWord, secondWord) == 1

firstWord = "road"
secondWord = "word"
assert s.minDistance(firstWord, secondWord) == 3

