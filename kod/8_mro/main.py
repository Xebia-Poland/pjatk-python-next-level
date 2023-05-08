class Animal(object):
    def __init__(self, name):
        self.nazwa = name

class Horse(Animal):
    def __init__(self, name, color):
        self.color = color
        Animal.__init__(self, name)

class Donkey(Animal):
    def __init__(self, name):
        super().__init__(name)

class Mule(Donkey, Horse):
    def __init__(self, name):
        # print()
        super().__init__(name)


print(Animal.mro())
print(Horse.mro())
print(Donkey.mro())
print(Mule.mro())
#

emule = Mule('Jonny')
