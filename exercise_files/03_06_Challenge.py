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

# ## Converting Hexadecimal to Decimal
#
# Hexadecimal or "base 16" uses all of the numbers 0 - 9, plus a few others to signify higher numbers:
#
# A = 10
#
# B = 11
#
# C = 12
#
# D = 13
#
# E = 14
#
# F = 15
#
# Therefore, the number 'D' in hexadecimal would be 13 in decimal.
#
# The number '1A' in hexadecimal would be 26 in decimal. Just like we have the "tens" place in base 10, hexadecimal has the "sixteens" place. So 1A would be 16 + 10 or 26.
#
# And just like decimal has the "hundreds" place (because 10 * 10 is 100), hexadecimal has the "256's" place (because 16 * 16 is 256) So 'ABC' in hexadecimal is (256 * 10) + (16 * 11) + (1 * 12) or 2,748
#

# +
hexNumbers = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
}


# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    pass


# -

# 10
hexToDec("A")

# 0
hexToDec("0")

# 27
hexToDec("1B")

# 960
hexToDec("3C0")

# None
hexToDec("A6G")

# None
hexToDec("ZZTOP")


