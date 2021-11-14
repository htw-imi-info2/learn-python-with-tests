import unittest

class TestSomething(unittest.TestCase):

    def test_loop_range(self):
        a = []
        for i in range(0,5):
            a.append(i)
        self.assertEqual([0,1,2,3,4],a)

if __name__ == '__main__':
    unittest.main()
