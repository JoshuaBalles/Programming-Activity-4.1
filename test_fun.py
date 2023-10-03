import unittest

def fun(x):
    return x+2

class myTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(4), 6)

if __name__ == '__main__':
    unittest.main()