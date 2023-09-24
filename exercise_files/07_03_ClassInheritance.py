# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# ## Class Inheritance


# +
class Dog:
    _legs = 4

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + " says: Bark!")

    def getLegs(self):
        return self._legs


class Chihuahua(Dog):
    def speak(self):
        print(f"{self.name} says: Yap yap yap!")

    def wagTail(self):
        print("Vigorous wagging!")


# -

dog = Chihuahua("Roxy")
dog.speak()
dog.wagTail()

myDog = Dog("Rover")
myDog.speak()

# ### Extending built-in classes

myList = list()


# +
class UniqueList(list):
    def append(self, item):
        if item in self:
            return
        super().append(item)


uniqueList = UniqueList()
uniqueList.append(1)
uniqueList.append(1)
uniqueList.append(2)

print(uniqueList)


# +
class UniqueList(list):
    def __init__(self):
        super().__init__()
        self.someProperty = "Unique List!"

    def append(self, item):
        if item in self:
            return
        super().append(item)


uniqueList = UniqueList()
uniqueList.append(1)
uniqueList.append(1)
uniqueList.append(2)

print(uniqueList.someProperty)
# -

