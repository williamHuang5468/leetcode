'''
Two Way:
1. 暴力法
2. build-in
'''

# Build-in
class Solution(object):
    def detectCapitalUse(self, word):
        return word.isupper() or word.istitle() or word.islower()

# 暴力
'''
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        All letters in this word are capitals, like "USA".
        All letters in this word are not capitals, like "leetcode".
        Only the first letter in this word is capital if it has more than one letter, like "Google".
        """
        if len(word) == 1:
            return True
        if self.isUpper(word[0]):
            up = self.isUpper(word[1]) # Second letter is lower or upper
            low = self.isLower(word[1])
            for letter in word[2:]:
                isUpperOrLower = (up and self.isUpper(letter)) or (low and self.isLower(letter))
                if not isUpperOrLower:
                    return False
            return True
        else:
            for letter in word[1:]:
                if self.isUpper(letter):
                    return False
            return True

    def isUpper(self, letter):
        return ord(letter) < 97
    def isLower(self, letter):
        return ord(letter) > 96
'''