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

# ### Challenge Hints!

# **HINT 1:** You can figure out whether a variable is of a certain type in the following way:
#

# +
myVar = 1

if type(myVar) == int:
    print("myVar is an integer!")

if type(myVar) != int:
    print("myVar is NOT an integer!")
# -

# **HINT 2:** You can create a while loop and manipulate multiple variables inside of it:

# +
# This prints the sum of all of the numbers from 1 to 10
i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i

s
# -


# **HINT 3:** Alternatively, a function can call itself! This is called "recursion" This also returns the sum of all numbers from 0 to 10:
#


# +
def addNumbers(i):
    if i == 0:
        return 0
    return i + addNumbers(i - 1)


addNumbers(10)


# -


# Returns the value of the factorial of num if it is defined, otherwise, returns None
def factorial(num):
    pass


factorial(5)

factorial(0)

factorial(-2)

factorial(1.2)

factorial("spam spam spam spam spam spam")
