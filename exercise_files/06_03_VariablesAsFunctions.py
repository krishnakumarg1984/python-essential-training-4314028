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

# ## Variables as Functions

x = 5


def x():
    return 5


# ### Viewing function data with  \_\_code\_\_

print(x.__code__.co_varnames)
print(x.__code__.co_code)

# ### Text processing in Python

text = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""


# +
def lowercase(text):
    return text.lower()


def removePunctuation(text):
    punctuations = [".", "-", ",", "*"]
    for punctuation in punctuations:
        text = text.replace(punctuation, "")
    return text


def removeNewlines(text):
    text = text.replace("\n", " ")
    return text


def removeShortWords(text):
    return " ".join([word for word in text.split() if len(word) > 3])


def removeLongWords(text):
    return " ".join([word for word in text.split() if len(word) < 6])


# +
processingFunctions = [lowercase, removePunctuation, removeNewlines, removeLongWords]

for func in processingFunctions:
    text = func(text)

print(text)
# -

# ### Lambda functions

2 + 3

(lambda x: x + 3)(5)

myList = [5, 4, 3, 2]
sorted(myList)

myList = [{"num": 3}, {"num": 2}, {"num": 1}]
sorted(myList, key=lambda x: x["num"])


