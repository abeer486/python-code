class Dog(object):
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in a response to a command."""
        print(self.name.title() + " is now sitting.")

    def laugh(self):
        """Simulate a dog chuckle"""
        print(self.name.title() + " is now laughing.")

my_dog = Dog('Mutley', 10)
print(my_dog.name.title())
my_dog.laugh()
my_dog.sit()
