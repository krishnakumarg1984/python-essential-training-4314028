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

# ## ASCII Art Encoding
#
# Write a function "encodeString" that will encode a string like 'AAAAABBBBAAA' as a list of tuples: [('A', 5), ('B', 4), ('A', 3)] meaning that the string has "5 A's, followed by 4 B's, followed by 3 A's"
#
# Then use that function to compress a string containing "ASCII Art" (https://en.wikipedia.org/wiki/ASCII_art)
#
# Write a corresponding function "decodeString" that will take in a list of tuples and print the original string.
#


# +

from typing import List, Tuple


def encodeString(stringVal: str) -> List[Tuple[str, int]]:
    last_char = ""
    count = 0
    encodedList = []
    for char in stringVal:
        if last_char == "":
            last_char = char
            count += 1
        elif char == last_char:
            count += 1
        elif char != last_char:
            encodedList.append((last_char, count))
            last_char = char
            count = 1
    if count > 0:
        encodedList.append((last_char, count))

    return encodedList


def decodeString(encodedList) -> str:
    decodedStr = ""
    for char in encodedList:
        decodedStr += char[0] * char[1]
    return decodedStr


# -

art = """



                               %%%%%%%%%%%%%%%%%%%
                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                    %%%%%%%%                         %%%%%%%%
                %%%%%%%                                   %%%%%%
              %%%%%%                                         %%%%%%
           %%%%%%                                               %%%%%
          %%%%%                                                   %%%%%
        %%%%%                                                       %%%%%
       %%%%                 %%%%%              %%%%%                  %%%%
      %%%%                 %%%%%%%            %%%%%%%                  %%%%
     %%%%                  %%%%%%%            %%%%%%%                   %%%%
    %%%%                   %%%%%%%            %%%%%%%                    %%%%
    %%%%                    %%%%%              %%%%%                     %%%%
   %%%%                                                                   %%%%
   %%%%                                                                   %%%%
   %%%%                                                                   %%%%
   %%%%                                                      %%%%        %%%%
    %%%%       %%%%%%                                        %%%%%       %%%%
    %%%%         %%%%                                       %%%%        %%%%
     %%%%         %%%%                                     %%%%         %%%%
      %%%%         %%%%%                                  %%%%         %%%%
       %%%%%         %%%%%                             %%%%%         %%%%%
        %%%%%          %%%%%%                        %%%%%          %%%%
          %%%%%           %%%%%%%               %%%%%%%           %%%%%
            %%%%%             %%%%%%%%%%%%%%%%%%%%%             %%%%%
              %%%%%%%                                        %%%%%
                 %%%%%%%                                 %%%%%%%
                     %%%%%%%%%                     %%%%%%%%%
                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                   %%%%%%%%%%%%



"""

# print(decodeString(encodeString("AAAAABBBBAAA")))
encodedString = encodeString(art)

print(decodeString(encodedString))
