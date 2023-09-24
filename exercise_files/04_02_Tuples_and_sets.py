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

# ## Sets

mySet = {"a", "b", "c"}
mySet

mySet = set(("a", "b", "c"))

mySet

myList = ["a", "b", "b", "c", "c"]
myList = list(set(myList))
myList

mySet[0]

number = 1
1[0]

mySet.add("d")
mySet

"a" in mySet

"z" in mySet

len(mySet)

while len(mySet):
    print(mySet.pop())

mySet

mySet = {"a", "b", "c"}

mySet.discard("a")

mySet

# ## Tuples

myTuple = ("a", "b", "c")
myTuple

myTuple[0]

myTuple[0] = "d"


# +
def returnsMultipleValues():
    return 1, 2, 3


type(returnsMultipleValues())
# -

myTuple = (1, 2, 3)

type(myTuple)

a, b, c = returnsMultipleValues()

print(a)
print(b)
print(c)


