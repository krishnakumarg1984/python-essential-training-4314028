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

# ## Class

# ### Instance Attributes


# +
class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + " says: Bark!")


myDog = Dog("Rover")
print(myDog.name)
print(myDog.legs)
# -

Dog.legs


# ### Static Attributes


# +
class Dog:
    legs = 4

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + " says: Bark!")


myDog = Dog("Rover")
print(myDog.name)
print(myDog.legs)
# -

Dog.legs

Dog.legs = 3

myDog = Dog("Rover")
print(myDog.name)
print(myDog.legs)


# +
class Dog:
    _legs = 4

    def __init__(self, name):
        self.name = name

    def getLegs(self):
        return self._legs

    def speak(self):
        print(self.name + " says: Bark!")


myDog = Dog("Rover")
print(myDog.name)
print(myDog.getLegs())
# -

myDog = Dog("Rover")
myDog._legs = 3
print(myDog.name)
print(myDog.getLegs())
print(Dog._legs)


