import unittest
from projectJ_29 import countm


class Testcountm(unittest.TestCase):
    def test_simple(self):
        s = "mohammad"
        m = "m"
        self.assertEqual(countm(s, m), 3)

    def test_nothing(self):
        s = ""
        m = "m"
        self.assertEqual(countm(s, m), 0)

    def test_longer(self):
        s = "mohammad mohammad mohammad"
        m = "m"
        self.assertEqual(countm(s, m), 9)

    def test_non_existence(self):
        s = "mohammad"
        m = "q"
        self.assertEqual(countm(s, m), 0)

    def test_all(self):
        s = "wwwww"
        m = "w"
        self.assertEqual(countm(s, m), 4)


if __name__ == "__main__":
    unittest.main()
