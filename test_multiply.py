import unittest

def fun(x, y):
    return x*y

class myTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(6,6), 36)

if __name__ == '__main__':
    unittest.main()