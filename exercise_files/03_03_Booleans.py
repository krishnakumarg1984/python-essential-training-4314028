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

# ## Booleans

# ### Casting Booleans

bool(1)

bool(0)

bool(-1)

bool(1j)

bool(0.0)

bool(0j)

bool("True")

bool("False")

bool("")

bool([1, 2])

bool({})

bool(None)

myList = [1, 2]
if bool(myList):
    print("Mylist has some values in it!")

a = 5
b = 5
if a - b:
    print("a and b are not equal!")

a == b

# ### Boolean Logic

# +
weatherIsNice = True
haveUmbrella = False

if not (haveUmbrella or weatherIsNice):
    print("Stay inside")
else:
    print("Go for a walk")

# +
weatherIsNice = True
haveUmbrella = False

if (not haveUmbrella) and (not weatherIsNice):
    print("Stay inside")
else:
    print("Go for a walk")

# +
weatherIsNice = True
haveUmbrella = False

if haveUmbrella or weatherIsNice:
    print("Go for a walk")
else:
    print("Stay inside")
# -

