import unittest

class TestSomething(unittest.TestCase):

    def test_a_string_variable(self):
        a = "Hello,  world!"
        self.assertEqual("Hello,  world!",a)

if __name__ == '__main__':
    unittest.main()
