import unittest

def broken_function():
    raise Exception('This is broken')

class TestSomething(unittest.TestCase):

    def test_a_string_variable(self):
        a = "Hello,  world!"
        self.assertEqual("Hello,  world!", a)

    def test_expect_an_exception(self):
        with self.assertRaises(Exception):
            broken_function()

    def test_undefined_as_example(self):
        with self.assertRaises(NameError):
            a = notdefined


if __name__ == '__main__':
    unittest.main()
