import unittest

class TestCoreFunctions(unittest.TestCase):

    def test_reverse_range(self):
        self.assertEqual(list(reversed(range(0,11))), [10,9,8,7,6,5,4,3,2,1,0])

    def test_count_char(self):
        s = "foobarfoobarfoobarfoobarfoobarfoobar"
        self.assertEqual(len(s.split(" ")), 8)

if __name__ == '__main__':
    unittest.main()
