import unittest

def check(x):
    return x >= 100

class myTest(unittest.TestCase):
    def test(self):
        self.assertTrue(check(101))

if __name__ == '__main__':
    unittest.main()