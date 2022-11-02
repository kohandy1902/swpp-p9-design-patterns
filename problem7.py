class Dog:
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof!"


class Person:
    def __init__(self):
        self.name = "Human"

    def talk(self):
        return "talk"


class Adapter:
    def __init__(self, obj, **adapted_methods):
        # TODO: fill this
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        # TODO: fill this
        return getattr(self.obj, attr)


if __name__ == "__main__":
    dog = Dog()
    talkable = Adapter(dog, talk=dog.bark)
    print(talkable.name)
    print(talkable.talk())
