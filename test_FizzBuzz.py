import unittest
import FizzBuzz

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(FizzBuzz, " ")

if __name__ == "__main__":
    unittest.main(verbosity=2)