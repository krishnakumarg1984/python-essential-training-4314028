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
#     display_name: Python 3.10.4 64-bit
#     language: python
#     name: python3
# ---

# ## ASCII Art Compression
#
# Use the "encodeString" and "decodeString" functions from the Chapter 4 challenge, provided below
#
# Read in the ASCII art text file 10_04_challenge_art.txt and write it back to a new file that has a smaller file size than the original file.
# For example, the original 10_04_challenge_art.txt has a file size of 2.757kB (or 2,757 ASCII characters).
#
# - Any compression is great!
# - Is there any way you could get this file to 1kb?
# - Less than 1kb?
#
# After compressing the file, make sure to check your work by opening and decoding it again!
#
#

# **HINT 1:** Doing something like this will technically meet the requirements of this challenge:

# +
import os

json.dumps(encodeString(text))
# -

# However, I hope you can find a more efficient compression algorithm than that!

# **HINT 2:** Writing a list of tuples, there are a lot of instances of "),(" and lots of extra quotes and things, which is a lot of characters to devote to where perhaps a single comma would suffice...

# **HINT 3:** If you're looking for a longer challenge, you can look into writing bytes to a file. This is absolutely not necessary, however!

# +


def encodeString(stringVal):
    encodedList = []
    prevChar = None
    count = 0
    for char in stringVal:
        if prevChar != char and prevChar is not None:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count = count + 1
    encodedList.append((prevChar, count))
    return encodedList


def decodeString(encodedList):
    decodedStr = ""
    for item in encodedList:
        decodedStr = decodedStr + item[0] * item[1]
    return decodedStr


# +


def encodeFile(filename, newFilename):
    # Your code here!
    pass


def decodeFile(filename):
    # Your code here!
    pass


# +
print(f'Original file size: {os.path.getsize("10_04_challenge_art.txt")}')

encodeFile("10_04_challenge_art.txt", "10_04_challenge_art_encoded.txt")

print(f'New file size: {os.path.getsize("10_04_challenge_art_encoded.txt")}')
# -


decodeFile("10_04_challenge_art_encoded.txt")


