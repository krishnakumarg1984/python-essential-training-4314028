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

# ## Factorial Challenge
#
# The factorial function gives the number of possible arrangements of a set of items of length "n"
#
# For example, there are 4! ("four factorial") or 24 ways to arrange four items, which can be calculated as:
# 4 \* 3 \* 2 \* 1
#
# 5! = 5 \* 4 \* 3 \* 2 \* 1 = 120
#
# 6! = 6 \* 5 \* 4 \* 3 \* 2 \* 1 = 720
#
# etc.
#
# In a set of 0 items (an empty set) there is only one way to arrange the items, therefore, 0! = 1
#
# For the purposes of this exercise, factorials are only defined for **positive integers** (including 0)
#
#
#


# Returns the value of the factorial of num if it is defined, otherwise, returns None
from typing_extensions import Optional


def factorial(num: int) -> Optional[int]:
    if not isinstance(num, int) or num < 0:
        return None
    if num == 0:
        return 1
    return num * factorial(num - 1)


# return 120
print(factorial(5))

# return 720
print(factorial(6))

# return 1
print(factorial(0))

# return None
print(factorial(-2))

# return None
print(factorial(1.2))

# return None
print(factorial("spam spam spam spam spam spam"))
