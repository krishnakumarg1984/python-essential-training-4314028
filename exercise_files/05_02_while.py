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

from datetime import datetime

# ## While loops

datetime.now().second

# +
wait_until = datetime.now().second + 2

while datetime.now().second != wait_until:
    print("Still waiting!")

print(f"We are at {wait_until} seconds!")

# +
wait_until = datetime.now().second + 2

while datetime.now().second != wait_until:
    1 + 1

print(f"We are at {wait_until} seconds!")
# -

# ### Pass

# +
wait_until = datetime.now().second + 2

while datetime.now().second != wait_until:
    pass

print(f"We are at {wait_until} seconds!")
# -

# ### Break

# +
wait_until = datetime.now().second + 2

while True:
    if datetime.now().second == wait_until:
        print(f"We are at {wait_until} seconds!")
        break

# +
wait_until = datetime.now().second + 2

while True:
    while datetime.now().second == wait_until:
        print(f"We are at {wait_until} seconds!")
        break
# -

# ### Continue

# +
wait_until = datetime.now().second + 2

while datetime.now().second != wait_until:
    continue
    print("Still waiting!")


print(f"We are at {wait_until} seconds!")

# +
wait_until = datetime.now().second + 2

while True:
    if datetime.now().second < wait_until:
        continue
    break


print(f"We are at {wait_until} seconds!")
# -

