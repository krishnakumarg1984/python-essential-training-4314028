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

# ## Functions

print("Hello, World!")


# +
def multiplyByThree(val):
    return 3 * val


multiplyByThree(4)


# -

def multiply(val1, val2):
    return val1 * val2


multiply(3, 4)

# +
a = [1, 2, 3]


def appendFour(myList):
    myList.append(4)


appendFour(a)
print(a)
# -

print(print("Hello, World!"))

type(None)

None + 1


