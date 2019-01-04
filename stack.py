import unittest

class TestUsingListAsStack(unittest.TestCase):
    # https://docs.python.org/3/tutorial/datastructures.html#looping-techniques

    def test_push_and_pop(self):
        stack = []
        stack.append(9)
        stack.append(3)
        stack.append("(")
        self.assertEqual("(",stack.pop())
        self.assertEqual(3,stack.pop())
        self.assertEqual(9,stack.pop())

    def test_better_push(self):
        stack = list(range(1,10))
        # seems only to work with own classes?
        with self.assertRaises(AttributeError): stack.push = stack.append

    def test_own_stack(self):
        # subclass list:
        # https://stackoverflow.com/questions/9432719/python-how-can-i-inherit-from-the-built-in-list-type
        class Stack(list):
            def __init__(self, *args):
                list.__init__(self, *args)

        stack = Stack([])
        stack.append(9)
        stack.append(3)

        self.assertEqual(3,stack.pop())
        self.assertEqual(9,stack.pop())

        # now, all good - I can add a push attribute:
        stack.push = stack.append
        stack.push(3)
        self.assertEqual(3,stack.pop())

if __name__ == '__main__':
    unittest.main()
