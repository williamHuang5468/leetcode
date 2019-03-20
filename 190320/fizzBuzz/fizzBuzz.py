class fizzBuzz(object):
    def __init__(self, n):
        self.n = n

    def output(self):
        return [self.checkCondition(i) for i in range(1, self.n+1)]

    def checkCondition(self, n):
        if n % 15 == 0:
            return "fizzbuzz"
        elif n % 5 == 0:
            return "buzz"
        elif n % 3 == 0:
            return "fizz"
        else:
            return str(n)
