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

import math

# ## Functions


# +
def performOperation(num1, num2, operation):
    if operation == "sum":
        return num1 + num2
    if operation == "multiply":
        return num1 * num2


performOperation(2, 3, "sum")
# -



# ### Named Parameters


# +
def performOperation(num1, num2, operation="sum"):
    if operation == "sum":
        return num1 + num2
    if operation == "multiply":
        return num1 * num2


performOperation(2, 3)


# +
def performOperation(num1, num2, operation="sum", message="Default message"):
    print(message)
    if operation == "sum":
        return num1 + num2
    if operation == "multiply":
        return num1 * num2


performOperation(2, 3, message="A new message!", operation="multiply")
# -


# ### *args


# +
def performOperation(*args):
    print(args)


performOperation(1, 2, 3)
# -

performOperation(1, 2, 3, operation="sum")


# ### **kwargs


# +
def performOperation(*args, **kwargs):
    print(args)
    print(kwargs)


performOperation(1, 2, 3, operation="sum")


# +
def performOperation(*args, operation="sum"):
    if operation == "sum":
        return sum(args)
    if operation == "multiply":
        return math.prod(args)


performOperation(1, 2, 3, 6, 7, 8, operation="sum")
# -

