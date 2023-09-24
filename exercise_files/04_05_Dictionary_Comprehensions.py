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

# ## Dictionary Comprehensions

animalList = [("a", "aardvark"), ("b", "bear"), ("c", "cat"), ("d", "dog")]
animals = {item[0]: item[1] for item in animalList}
animals

animals = {key: value for key, value in animalList}
animals

animals.items()

list(animals.items())

[{"letter": key, "name": value} for key, value in animals.items()]


