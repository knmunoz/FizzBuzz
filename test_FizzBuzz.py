import unittest
import FizzBuzz

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(FizzBuzz.multiples(3), "Fizz")
    def test2(self):
        self.assertEqual(FizzBuzz.multiples(15), "FizzBuzz")

if __name__ == "__main__":
    unittest.main(verbosity=2)