import unittest

class TestClasses(unittest.TestCase):

    def test_bark(self):
        class Dog:
            def bark(self):
                return "bark"

        d = Dog()
        self.assertEqual("bark",d.bark())

        # classes can be reopened
        class Dog:
        	def bark(self):
        		return "woooof"

        d1 = Dog()
        # bark method is overwritten
        self.assertEqual("woooof",d1.bark())

        # but not in the old instance!
        self.assertEqual("bark",d.bark())

if __name__ == '__main__':
    unittest.main()
