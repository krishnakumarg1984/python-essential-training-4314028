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

# ## Lists

# ### List Slicing

myList = [1, 2, 3, 4, 5]
myList[3:]

myList[0:6:2]

myList[0:6:3]

myList[::2]

for i in range(100):
    print(i)

myList = list(range(100))

myList[::10]

myList[::-10]

# ### Modifying Lists

myList = [1, 2, 3, 4]
myList.append(5)
print(myList)

myList.insert(3, "a new value")
print(myList)

myList.remove("a new value")

myList

myList.pop()

myList

while len(myList):
    print(myList.pop())

myList

a = [1, 2, 3, 4, 5]
b = a
a.append(6)
print(b)

a = [1, 2, 3, 4, 5]
b = a.copy()
a.append(6)
print(a)
print(b)

for i in range(20):
    print(i)


