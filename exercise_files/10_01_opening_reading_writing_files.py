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

# ## Files

# ### Reading Files

f = open("10_01_file.txt", "r")
print(f)

f.readline()

f.readlines()

f = open("10_01_file.txt", "r")
for line in f.readlines():
    print(line.strip())

# ### Writing Files

f = open("10_01_output.txt", "w")
print(f)

f.write("Line 1\n")
f.write("Line 2\n")

f.close()

# ### Appending Files

f = open("10_01_output.txt", "a")
f.write("Line 3\n")
f.write("Line 4\n")
f.close()

# +
with open("10_01_output.txt", "a") as f:
    f.write("some stuff\n")
    f.write("some other stuff\n")

print(f)
# -

f.write("PS. I forgot some stuff")


