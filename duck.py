import unittest

class Duck:
    def quack(self):
    	return "quaaack!"
class Dog:
    def bark(self):
	    return "woooof!"

def func(maybe_a_duck):
	return "let it quack: " + maybe_a_duck.quack()

class TestDuckTyping(unittest.TestCase):

    def test_ducks_quack(self):
        duck = Duck()
        self.assertEqual("let it quack: quaaack!",func(duck))

    def test_dogs_dont_quack(self):
        dog = Dog()
        with self.assertRaises(AttributeError): func(dog)

    def test_make_this_dog_quack(self):
        dog = Dog()
        dog.quack = dog.bark
        self.assertEqual("let it quack: woooof!",func(dog))

if __name__ == '__main__':
    unittest.main()
