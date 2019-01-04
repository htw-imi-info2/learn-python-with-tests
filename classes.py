
class Dog:
	def bark(self):
		return "woof"

d = Dog()
print(d.bark())

# classes can be reopened
class Dog:
	def bark(self):
		return "woooof"

d1 = Dog()
# bark method is overwritten
print(d1.bark())
# but not in the old instance!
print(d.bark())
