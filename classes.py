import unittest

class Dog:
	def bark(self):
		return "woof"

d = Dog()

# classes can be reopened
class Dog:

	def bark(self):
		return "woooof"

d1 = Dog()

# bark method is overwritten
# print(d1.bark())

class TestClasses(unittest.TestCase):
	def test_bark_method_is_overwritten(self):
		self.assertEqual("woooof",d1.bark())

# but not in the old instance!
# print(d.bark())
	def test_but_not_in_the_old_instance(self):
		self.assertEqual("woof",d.bark())


if __name__ == '__main__':
    unittest.main()
