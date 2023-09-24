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

# ## Control Flow

# ### If / Else statements

a = True
if a:
    print("It is true!")
    print("Also print this")
else:
    print("It is false!")
print("Always print this")

a = True
b = False
c = True
if a:
    print("It is true!")
    print("Also print this")
    if b:
        print("Both are true")
        if c:
            print("All three are true")
else:
    print("It is false!")
print("Always print this")

# ### For loops

a = [1, 2, 3, 4, 5]
for number in a:
    print(number)

4 in a

# ### While loops

a = 0
while a < 5:
    print(a)
    a = a + 1


