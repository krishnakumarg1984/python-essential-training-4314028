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

# ## For

myList = [1, 2, 3, 4]
for item in myList:
    print(item)

# ### Pass

# +
animalLookup = {
    "a": ["aardvark", "antelope"],
    "b": ["bear"],
    "c": ["cat"],
    "d": ["dog"],
}

for letter, animals in animalLookup.items():
    pass
# -


# ### Continue

for letter, animals in animalLookup.items():
    if len(animals) > 1:
        continue
    print(f"Only one animal! {animals[0]}")

# ### Break

for letter, animals in animalLookup.items():
    if len(animals) > 1:
        print(f"Found {len(animals)} animals: {animals}")
        break

# ### For / Else

for number in range(2, 100):
    for factor in range(2, int(number**0.5) + 1):
        if number % factor == 0:
            break
    else:
        print(f"{number} is prime!")


for number in range(2, 100):
    found_factors = False
    for factor in range(2, int(number**0.5) + 1):
        if number % factor == 0:
            found_factor = True
    if not found_factors:
        print(f"{number} is prime!")


