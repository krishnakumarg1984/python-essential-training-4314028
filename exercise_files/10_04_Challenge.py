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

# +
import os

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
    decodedStr = ''
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

encodeFile('10_04_challenge_art.txt', '10_04_challenge_art_encoded.txt')

print(f'New file size: {os.path.getsize('10_04_challenge_art_encoded.txt')}')

# -

decodeFile('10_04_challenge_art_encoded.txt')


