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

import json
from json import JSONDecodeError, JSONEncoder

# ## JSON

# ### Loading JSON

jsonString = '{"a": "apple", "b": "bear", "c": "cat",}'
try:
    json.loads(jsonString)
except JSONDecodeError:
    print("Could not parse JSON!")

{
    "a": "apple",
    "b": "bear",
    "c": "cat",
}

# ### Dumping JSON

pythonDict = {
    "a": "apple",
    "b": "bear",
    "c": "cat",
}
json.dumps(pythonDict)


# ### Custom JSON Decoders


# +
class Animal:
    def __init__(self, name):
        self.name = name


class AnimalEncoder(JSONEncoder):
    def default(self, o):
        if type(o) == Animal:
            return o.name
        return super().default(o)


pythonDict = {
    "a": Animal("aardvark"),
    "b": Animal("bear"),
    "c": Animal("cat"),
}
json.dumps(pythonDict, cls=AnimalEncoder)
# -

