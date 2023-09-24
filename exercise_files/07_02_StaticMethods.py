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

# ## Static and Instance Methods


# +
class WordSet:
    def __init__(self):
        self.words = set()

    def addText(self, text):
        text = WordSet.cleanText(text)
        for word in text.split():
            self.words.add(word)

    def cleanText(text):
        # chaining functions
        text = text.replace("!", "").replace(".", "").replace(",", "").replace("'", "")
        return text.lower()


wordSet = WordSet()

wordSet.addText("Hi, I'm Ryan! Here is a sentence I want to add!")
wordSet.addText("Here is another sentence I want to add.")

print(wordSet.words)


# +
class WordSet:
    replacePuncs = ["!", ".", ",", "'"]

    def __init__(self):
        self.words = set()

    def addText(self, text):
        text = WordSet.cleanText(text)
        for word in text.split():
            self.words.add(word)

    def cleanText(text):
        # chaining functions
        for punc in WordSet.replacePuncs:
            text = text.replace(punc, "")
        return text.lower()


wordSet = WordSet()

wordSet.addText("Hi, I'm Ryan! Here is a sentence I want to add!")
wordSet.addText("Here is another sentence I want to add.")

print(wordSet.words)
# -



# ### Decorators


# +
class WordSet:
    replacePuncs = ["!", ".", ",", "'"]

    def __init__(self):
        self.words = set()

    def addText(self, text):
        text = self.cleanText(text)
        for word in text.split():
            self.words.add(word)

    @staticmethod
    def cleanText(text):
        # chaining functions
        for punc in WordSet.replacePuncs:
            text = text.replace(punc, "")
        return text.lower()


wordSet = WordSet()

wordSet.addText("Hi, I'm Ryan! Here is a sentence I want to add!")
wordSet.addText("Here is another sentence I want to add.")

print(wordSet.words)
# -

