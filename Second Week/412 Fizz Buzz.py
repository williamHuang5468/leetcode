class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list = []
        for i in range(1, n+1):
            isFizz = i % 3 == 0
            isBuzz = i % 5 == 0
            if isFizz or isBuzz:
                if isFizz and isBuzz:
                    list.append("FizzBuzz")
                elif isFizz:
                    list.append("Fizz")
                elif isBuzz:
                    list.append("Buzz")
            else:
                list.append(str(i))
        return list
