from fizzBuzz import *
import unittest


class testFizzBuzz(unittest.TestCase):
    def test_first(self):
        f = fizzBuzz(2)
        expected = ["1", "2"]
        self.assertEquals(expected, f.output())

    def test_fizz(self):
        f = fizzBuzz(3)
        expected = ["1", "2", "fizz"]
        self.assertEquals(expected, f.output())

    def test_buzz(self):
        f = fizzBuzz(5)
        expected = ["1", "2", "fizz", "4", "buzz"]
        self.assertEquals(expected, f.output())

    def test_fizzBuzz(self):
        f = fizzBuzz(15)
        expected = ["1", "2", "fizz", "4", "buzz", "fizz", "7",
                    "8", "fizz", "buzz", "11", "fizz", "13", "14", "fizzbuzz"]
        self.assertEquals(expected, f.output())
