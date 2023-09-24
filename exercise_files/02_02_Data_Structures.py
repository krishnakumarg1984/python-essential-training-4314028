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

# # Data Structures

# ## Lists

my_list = [1, 2, 3, 4]
print(my_list)

my_list = ["list", "of", "strings"]

my_list = [1, "list", False, []]

my_list = [[1, 2, 3], [False, True], []]

len(my_list)

# ## Sets

my_set = {1, 2, 3, 4, 5}
print(my_set)

type(my_set)

len(my_set)

my_set = {1, 1, 2, 2}
len(my_set)
print(my_set)

[1, 2] == [2, 1]

{1, 2, 3} == {3, 2, 1, 1, 1}

# ## Tuples

my_tuple = (1, 2, 3)

len(my_tuple)

(1, 2) == (2, 1)

my_list.append(6)
print(my_list)

my_tuple.append(4)

# ## Dictionaries

my_dictionary = {"apple": "A red fruit", "bear": "A scary animal"}

my_dictionary["apple"]

my_dictionary = {
    "apple": "A red fruit",
    "bear": "A scary animal",
    "apple": "Sometimes a green fruit",
}

my_dictionary["apple"]


