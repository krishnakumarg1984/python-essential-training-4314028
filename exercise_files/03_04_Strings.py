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

# ## Strings

# ### Slicing

name = "My name is Ryan Mitchell"

name[0]

name[1]

name[0:7]

name[:7]

name[11:]

myList = [1, 2, 3, 4, 5]

myList[2:4]

len(name)

len(myList)

# ### Formatting

"My number is: " + str(5)

f"My number is: {5}"

f"My number is: {5} and twice that is {2*5}"

f"Pi is: {math.pi:.2f}"

"Pi is: {}".format(math.pi)

# ### Multi-line Strings

myString = """
Here is a long block of text
I can add newlines!
the text doesn't stop until it sees \'\'\'

"""

myString

print(myString)


